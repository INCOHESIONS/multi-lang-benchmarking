using System.IO;
using System.Diagnostics;
using System.Globalization;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.PixelFormats;
using System;
using System.Linq;

const string CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

string RandomCharacters(int length = 10)
{
    var random = new Random();
    return string.Join("", (from _ in Enumerable.Range(0, length) select CHARS[random.Next(0, CHARS.Length)]).ToArray()) ?? "error";
}

float SquaredDistance((int, int) p, int x, int y)
{
    int dx = x - p.Item1;
    int dy = y - p.Item2;
    return dx * dx + dy * dy;
}

var width = Convert.ToInt32(args[0]);
var height = Convert.ToInt32(args[1]);
var numberOfPoints = Convert.ToInt32(args[2]);
var saveImage = args[3] == "true";

var image = new Image<Rgba32>(Configuration.Default, width, height);

var random = new Random();
(int, int)[] points = [.. Enumerable.Range(0, numberOfPoints).Select(_ => (random.Next(0, width), random.Next(0, height)))];

var watch = new Stopwatch();
watch.Start();

for (int x = 0; x < width; x++)
    for (int y = 0; y < height; y++)
    {
        float minDist = float.PositiveInfinity;

        foreach (var p in points)
            minDist = MathF.Min(minDist, SquaredDistance(p, x, y));

        float color = (255.0F - Math.Clamp((float)Math.Sqrt(minDist), 0.0F, 255.0F)) / 255.0F;
        image[x, y] = new(color, color, color);
    }

watch.Stop();

Console.WriteLine((watch.ElapsedMilliseconds / 1000.0).ToString(CultureInfo.InvariantCulture));

if (!saveImage) return;

Directory.CreateDirectory("img/");
image.Save($"img/{RandomCharacters()}.png");
