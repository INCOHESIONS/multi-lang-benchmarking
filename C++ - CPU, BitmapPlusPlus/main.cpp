#include <algorithm>
#include <print>
#include <random>
#include <ranges>
#include <chrono>
#include <filesystem>
#include <algorithm>
#include <limits>
#include <cstdlib>

#include "BitmapPlusPlus.hpp"

#define RESULTS_DIRECTORY "./img/"

namespace
{
    int randint(const int min, const int max)
    {
        return rand() % (max - min + 1) + min;  // NOLINT
    }

    int randint(const int max)
    {
        return randint(0, max);
    }

    int as_int(const char* const c)
    {
        char *p;
        const long conv = strtol(c, &p, 10);

        if (errno != 0 || *p != '\0' || conv > INT_MAX || conv < INT_MIN)
            throw std::invalid_argument("Invalid integer conversion");

        return static_cast<int>(conv);  // assuming no errors
    }

    int squared_distance(const std::pair<int, int> p1, const int x, const int y)
    {
        const int dx = x - p1.first;
        const int dy = y - p1.second;
        return dx * dx + dy * dy;
    }

    constexpr std::string_view characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

    std::string random_characters(const int length = 10)
    {
        std::string str;

        for (int _ = 0; _ < length; _++)
            str += characters[randint(0, characters.length())];

        return str;
    }
}

int main(const int argc, const char* argv[])
{
    srand(time(nullptr));  // NOLINT

    if (argc != 5)
        throw std::invalid_argument("Usage: ./program.exe <width> <height> <number_of_points> <save image?>");

    const int width = as_int(argv[1]);
    const int height = as_int(argv[2]);
    const int number_of_points = as_int(argv[3]);
    const bool save_image = strcmp(argv[4], "false");

    if (width <= 0 || height <= 0 || number_of_points <= 0)
        throw std::invalid_argument("Usage: ./program.exe <width> <height> <number_of_points> <save image?>");

    std::vector<std::pair<int, int>> points;
    points.reserve(number_of_points);

    for (int _ = 0; _ < number_of_points; _++)
        points.emplace_back(randint(width), randint(height));

    bmp::Bitmap image(width, height);

    typedef std::chrono::high_resolution_clock clock;

    const auto t1 = clock::now();

    for (int x = 0; x < width; x++)
        for (int y = 0; y < height; y++)
        {
            int min_dist = std::numeric_limits<int>::max();

            for (const auto& p : points)
                min_dist = std::min(min_dist, squared_distance(p, x, y));

            const char c = static_cast<char>(255 - std::clamp(std::sqrt(min_dist), 0.0, 255.0));
            image.set(x, y, bmp::Pixel(c, c, c));
        }

    const auto t2 = clock::now();

    const std::chrono::duration<double> dt = t2 - t1;

    std::println("{}", dt.count());

    if (!save_image) return 0;

    if (!std::filesystem::exists(RESULTS_DIRECTORY))
        std::filesystem::create_directory(RESULTS_DIRECTORY);

    image.save(RESULTS_DIRECTORY + random_characters(10) + ".bmp");
}
