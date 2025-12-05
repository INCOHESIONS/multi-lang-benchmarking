const std = @import("std");
const zigimg = @import("zigimg");

const Point = struct {
    x: i32,
    y: i32,

    fn squared_dist(self: Point, x: i32, y: i32) u32 {
        const dx = x - self.x;
        const dy = y - self.y;
        return @intCast(dx * dx + dy * dy);
    }
};

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const alloc = gpa.allocator();
    defer _ = gpa.deinit();

    const argv = try std.process.argsAlloc(alloc);
    defer std.process.argsFree(alloc, argv);

    const width = try std.fmt.parseInt(usize, argv[1], 10);
    const height = try std.fmt.parseInt(usize, argv[2], 10);
    const number_of_points = try std.fmt.parseInt(usize, argv[3], 10);
    const save_image = std.mem.eql(u8, argv[4], "true");

    var points = try std.ArrayList(Point).initCapacity(alloc, number_of_points);
    defer points.deinit(alloc);

    var rng = std.Random.DefaultPrng.init(block: {
        var seed: u64 = undefined;
        std.crypto.random.bytes(std.mem.asBytes(&seed));
        break :block seed;
    });

    const random = rng.random();

    for (0..number_of_points) |_|
        try points.append(alloc, .{
            .x = random.intRangeAtMost(i32, 0, @intCast(width)),
            .y = random.intRangeAtMost(i32, 0, @intCast(height)),
        });

    const buffer_u8 = try alloc.alloc(u8, width * height * 3);
    var image = zigimg.Image{
        .width = width,
        .height = height,
        .pixels = try zigimg.color.PixelStorage.initRawPixels(buffer_u8, .rgb24),
    };

    defer image.deinit(alloc);

    var pixels = image.pixels.asBytes();

    @memset(pixels, 0);

    var timer = try std.time.Timer.start();

    for (0..width) |x| {
        for (0..height) |y| {
            var min_dist: u32 = std.math.maxInt(u32);

            for (points.items) |p|
                min_dist = @min(min_dist, p.squared_dist(@intCast(x), @intCast(y)));

            const color: u8 = @intCast(255 - std.math.clamp(std.math.sqrt(min_dist), 0, 255));

            const idx = (y * width + x) * 3;
            pixels[idx + 0] = color;
            pixels[idx + 1] = color;
            pixels[idx + 2] = color;
        }
    }

    const elapsed_ns = timer.read();

    var stdout_buffer: [1024]u8 = undefined;
    var stdout_writer = std.fs.File.stdout().writer(&stdout_buffer);
    const stdout = &stdout_writer.interface;

    const seconds = @as(f64, @floatFromInt(elapsed_ns)) / 1_000_000_000.0;
    try stdout.print("{}\n", .{seconds});
    try stdout.flush();

    if (!save_image) return;

    const filename = try randomString(alloc, random, 10);
    defer alloc.free(filename);

    const path = try std.fmt.allocPrint(alloc, "img/{s}.jpg", .{filename});
    defer alloc.free(path);

    try std.fs.cwd().makePath("img/");
    var file = try std.fs.cwd().createFile(path, .{});
    defer file.close();

    var write_buffer: [zigimg.io.DEFAULT_BUFFER_SIZE]u8 = undefined;

    try image.writeToFile(
        alloc,
        file,
        write_buffer[0..],
        zigimg.Image.EncoderOptions{ .jpeg = .{ .quality = 100 } },
    );
}

pub fn randomString(allocator: std.mem.Allocator, rand: std.Random, len: usize) ![]u8 {
    const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    const chars_len = chars.len;

    const buf = try allocator.alloc(u8, len);

    for (buf) |*c| {
        const idx = rand.uintLessThan(usize, chars_len);
        c.* = chars[idx];
    }

    return buf;
}
