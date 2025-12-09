// bmp_header and save() are based on https://github.com/baderouaich/BitmapPlusPlus/

#include <algorithm>  // std::clamp
#include <chrono>  // std::chrono::high_resolution_clock
#include <filesystem>  // std::filesystem
#include <fstream>  // std::ofstream
#include <print>  // std::println, std::numeric_limits

#define RESULTS_DIRECTORY "./img/"

namespace
{
    typedef std::chrono::high_resolution_clock clock;
    typedef std::pair<int, int> point;

#pragma pack(push, 1)
    struct bmp_header {
        /* Bitmap file header structure */
        std::uint16_t magic = 0x4D42;                                /* Magic number for file always BM which is 0x4D42 */  // NOLINT
        std::uint32_t file_size;                                     /* Size of file */  // NOLINT
        std::uint16_t reserved1 = 0;                                 /* Reserved */  // NOLINT
        std::uint16_t reserved2 = 0;                                 /* Reserved */  // NOLINT
        std::uint32_t offset_bits = sizeof(bmp_header);              /* Offset to bitmap data */  // NOLINT

        /* Bitmap file info structure */
        std::uint32_t size = 40;                                     /* Size of info header */  // NOLINT
        std::int32_t width;                                          /* Width of image */  // NOLINT
        std::int32_t height;                                         /* Height of image */  // NOLINT
        std::uint16_t planes = 1;                                    /* Number of color planes */  // NOLINT
        std::uint16_t bits_per_pixel = sizeof(std::uint8_t) * 3 * 8; /* Number of bits per pixel */  // NOLINT
        std::uint32_t compression = 0;                               /* Type of compression to use */  // NOLINT
        std::uint32_t size_image;                                    /* Size of image data */  // NOLINT
        std::int32_t x_pixels_per_meter = 0;                         /* X pixels per meter */  // NOLINT
        std::int32_t y_pixels_per_meter = 0;                         /* Y pixels per meter */  // NOLINT
        std::uint32_t clr_used = 0;                                  /* Number of colors used */  // NOLINT
        std::uint32_t clr_important = 0;                             /* Number of important colors */  // NOLINT

        bmp_header(const std::size_t width, const std::size_t height)
        : width(static_cast<std::int32_t>(width)),  // NOLINT
          height(static_cast<std::int32_t>(height)),
          file_size(bmp_size() + sizeof(bmp_header)),
          size_image(bmp_size()) { }

        [[nodiscard]] std::int32_t row_size() const
        {
            return width * 3 + width % 4;
        }

        [[nodiscard]] std::uint32_t bmp_size() const
        {
            return row_size() * height;
        }
    };
#pragma pack(pop)

    void save(
        const int width,
        const int height,
        const std::vector<std::uint8_t>& pixels,
        const std::filesystem::path& filename
    )
    {
        const bmp_header header(width, height);

        std::ofstream ofs{filename, std::ios::binary};

        if (!ofs.good())
            throw std::runtime_error("Unable to save bitmap file!");

        ofs.write(reinterpret_cast<const char*>(&header), sizeof(bmp_header));

        std::vector<std::uint8_t> line(header.row_size());
        for (std::int32_t y = height - 1; y >= 0; --y)
        {
            std::size_t i = 0;

            for (std::int32_t x = 0; x < width; ++x)
            {
                const std::uint8_t lightness = pixels[x + width * y];
                line[i++] = lightness;
                line[i++] = lightness;
                line[i++] = lightness;
            }

            ofs.write(
                reinterpret_cast<const char*>(line.data()),
                static_cast<std::streamsize>(line.size())
            );
        }
    }

    int randint(const int max)
    {
        return rand() % (max + 1); // NOLINT
    }

    int squared_distance(const point p, const int x, const int y)
    {
        const int dx = x - p.first;
        const int dy = y - p.second;
        return dx * dx + dy * dy;
    }

    constexpr std::string_view characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

    std::string random_characters(const int length = 10)
    {
        std::string str;

        for (int _ = 0; _ < length; _++)
            str += characters[randint(characters.length())];

        return str;
    }
}

int main([[maybe_unused]] const int _, const char* const argv[])
{
    const int width = std::stoi(argv[1]);
    const int height = std::stoi(argv[2]);
    const int number_of_points = std::stoi(argv[3]);
    const bool save_image = strcmp(argv[4], "false");

    if (width <= 0 || height <= 0 || number_of_points <= 0) throw std::invalid_argument("Invalid arguments");

    srand(time(nullptr)); // NOLINT

    std::vector<point> points(number_of_points);

    for (int _ = 0; _ < number_of_points; _++)
        points.emplace_back(randint(width), randint(height));

    std::vector<std::uint8_t> pixels(width * height); // NOLINT

    const auto start = clock::now();

    #pragma omp parallel for  // NOLINT
    for (int x = 0; x < width; x++)
    {
        for (int y = 0; y < height; y++)
        {
            int min_dist = std::numeric_limits<int>::max();

            for (const auto& p : points)
                min_dist = std::min(min_dist, squared_distance(p, x, y));

            pixels[x + width * y] = static_cast<std::uint8_t>(255 - std::clamp(std::sqrt(min_dist), 0.0, 255.0));
        }
    }

    const auto end = clock::now();

    const std::chrono::duration<double, std::nano> dt = end - start;

    std::println("{}", dt.count());

    if (!save_image) return 0;

    if (!std::filesystem::exists(RESULTS_DIRECTORY))
        std::filesystem::create_directory(RESULTS_DIRECTORY);

    save(width, height, pixels, RESULTS_DIRECTORY + random_characters() + ".bmp");
}
