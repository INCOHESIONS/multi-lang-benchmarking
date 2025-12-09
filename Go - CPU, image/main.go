package main

import (
	"fmt"
	"image"
	"image/color"
	"image/png"
	"math"
	"math/rand"
	"os"
	"path/filepath"
	"strconv"
	"time"
)

func main() {
	const PATH = "img/image.png"

	width, _ := strconv.Atoi(os.Args[1])
	height, _ := strconv.Atoi(os.Args[2])
	numberOfPoints, _ := strconv.Atoi(os.Args[3])
	saveImage := os.Args[4] == "true"

	points := generatePoints(width, height, numberOfPoints)

	imgRect := image.Rectangle{image.Point{0, 0}, image.Point{width, height}}

	img := image.NewGray(imgRect)

	start := time.Now()

	for x := range width {
		for y := range height {
			minDistance := math.MaxInt

			for _, p := range points {
				minDistance = min(minDistance, squaredDistance(p, x, y))
			}

			color := color.Gray{255 - uint8(clamp(int(math.Sqrt(float64(minDistance))), 0, 255))}

			img.Set(x, y, color)
		}
	}

	end := time.Now()

	fmt.Printf("%d", end.Sub(start).Nanoseconds())

	if !saveImage {
		return
	}

	dirs := filepath.Dir(PATH)

	if dirs != "." && dirs != "/" {
		os.MkdirAll(dirs, 0777)
	}

	file, err := os.Create(PATH)

	if err != nil {
		fmt.Printf("Something went wrong when creating a file at path %v\n", PATH)
		return
	}

	defer file.Close()

	png.Encode(file, img)
}

func squaredDistance(p image.Point, x, y int) int {
	dx := x - p.X
	dy := y - p.Y
	return dx*dx + dy*dy
}

func generatePoints(width, height, numberOfPoints int) []image.Point {
	points := make([]image.Point, numberOfPoints)

	for range points {
		points = append(points, image.Point{
			rand.Intn(width + 1),
			rand.Intn(height + 1),
		})
	}

	return points
}

func clamp(value, minimum, maximum int) int {
	return max(minimum, min(value, maximum))
}
