import { createCanvas } from "canvas";
import fs from "fs";

function random(min: number, max: number) {
    return Math.random() * (max - min) + min;
}

function squared_dist(p: Array<number>, x: number, y: number): number {
    const dx = x - p[0];
    const dy = y - p[0];
    return dx * dx + dy * dy;
}

function clamp(value: number, min: number, max: number) {
    return Math.min(Math.max(value, min), max);
}

function randomCharacters(length = 10) {
    const chars =
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    let result = "";

    for (let _ = 0; _ < length; _++)
        result += chars[Math.floor(Math.random() * chars.length)];

    return result;
}

const width = parseInt(process.argv[2]);
const height = parseInt(process.argv[3]);
const numberOfPoints = parseInt(process.argv[4]);
const saveImage = process.argv[5] == "true";

const points: Array<Array<number>> = [];

for (let i = 0; i < numberOfPoints; i++)
    points.push([random(0, width), random(0, height)]);

const canvas = createCanvas(width, height);
const ctx = canvas.getContext("2d");

const start = performance.now();

for (let x = 0; x < width; x++)
    for (let y = 0; y < height; y++) {
        let minDist = Number.MAX_VALUE;

        for (const p of points)
            minDist = Math.min(minDist, squared_dist(p, x, y));

        const color = 255 - clamp(Math.sqrt(minDist), 0, 255);

        ctx.fillStyle = `rgba(${color}, ${color}, ${color}, 1)`;
        ctx.fillRect(x, y, 1, 1);
    }

const end = performance.now();

console.log((end - start) / 1000);

if (!saveImage) process.exit();

const buffer = canvas.toBuffer("image/png");

if (!fs.existsSync("img/")) fs.mkdirSync("img/", { recursive: true });

fs.writeFileSync(`img/${randomCharacters()}.png`, buffer);
