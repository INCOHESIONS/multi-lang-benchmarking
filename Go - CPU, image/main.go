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

type Point struct {
	x int
	y int
}

func (p1 Point) distance(x, y int) int {
	return int(math.Hypot(float64(x-p1.x), float64(y-p1.y)))
}

func main() {
	const PATH = "img/image.png"

	width, _ := strconv.Atoi(os.Args[1])
	height, _ := strconv.Atoi(os.Args[2])
	numberOfPoints, _ := strconv.Atoi(os.Args[3])
	saveImage := os.Args[3] == "true"

	points := generatePoints(width, height, numberOfPoints)

	start := time.Now()

	img := generateImage(width, height, points)

	end := time.Now()

	fmt.Printf("%f", end.Sub(start).Seconds())

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

func generateImage(width, height int, points []Point) *image.Gray {
	upperLeft := image.Point{0, 0}
	bottomRight := image.Point{width, height}
	imgRect := image.Rectangle{upperLeft, bottomRight}

	img := image.NewGray(imgRect)

	for x := range width {
		for y := range height {
			minDistance := math.MaxInt

			for _, p := range points {
				minDistance = min(minDistance, p.distance(x, y))
			}

			color := color.Gray{255 - uint8(clamp(minDistance, 0, 255))}

			img.Set(x, y, color)
		}
	}

	return img
}

func generatePoints(width, height, numberOfPoints int) []Point {
	points := make([]Point, numberOfPoints)

	for range points {
		points = append(points, Point{
			randomRange(0, width),
			randomRange(0, height),
		})
	}

	return points
}

func clamp(value, minimum, maximum int) int {
	return max(minimum, min(value, maximum))
}

func randomRange(min, max int) int {
	return rand.Intn(max-min+1) + min
}

func input(msg string) int {
	var n int
	fmt.Print(msg)
	fmt.Scan(&n)
	return n
}
