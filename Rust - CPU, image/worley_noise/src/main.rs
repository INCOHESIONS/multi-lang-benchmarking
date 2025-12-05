use image::{GrayImage, Luma};
use rand::prelude::*;

fn main() {
    let args: Vec<String> = std::env::args().collect();

    let width = args[1].parse::<u32>().unwrap();
    let height = args[2].parse::<u32>().unwrap();
    let number_of_points = args[3].parse::<u32>().unwrap();
    let save_image = args[4] == "true";

    let mut rng = rand::thread_rng();

    let points: Vec<_> = (0..number_of_points)
        .map(|_| (rng.gen_range(0..width), rng.gen_range(0..height)))
        .collect();

    let instant = std::time::Instant::now();

    let img = GrayImage::from_fn(width, height, |x, y| {
        let closest = points.iter().map(|p| dist(p, x, y)).min().unwrap();
        Luma([255 - closest.clamp(0, 255) as u8])
    });

    let elapsed = instant.elapsed().as_secs_f64();

    println!("{elapsed}");

    if !save_image {
        return;
    }

    let path = format!("img/{}.png", generate_random_characters(10));

    if let Some(dirs) = std::path::Path::new(&path).parent() {
        std::fs::create_dir_all(dirs).expect("Couldn't create directories.");
    }

    img.save(&path)
        .expect(&format!("Unable to save image at path {}", &path));
}

const ASCII_LOWERCASE: &str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

fn generate_random_characters(length: usize) -> String {
    let mut rng = rand::thread_rng();

    (0..length)
        .map(|_| ASCII_LOWERCASE.chars().choose(&mut rng).unwrap())
        .collect()
}

fn dist(p: &(u32, u32), x: u32, y: u32) -> u32 {
    let a = p.0 - x;
    let b = p.1 - y;
    (a * a + b * b).isqrt() as u32
}
