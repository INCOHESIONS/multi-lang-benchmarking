import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Random;
import javax.imageio.ImageIO;

public class WorleyNoise {

    private record Point(int x, int y) {
        public int squaredDistance(final int x, final int y) {
            final int dx = x - this.x;
            final int dy = y - this.y;
            return dx * dx + dy * dy;
        }
    }

    public static void main(final String[] args) {
        final var width = Integer.parseInt(args[0]);
        final var height = Integer.parseInt(args[1]);
        final var numberOfPoints = Integer.parseInt(args[2]);
        final var saveImage = args[3].strip().equals("true");

        final var image = new BufferedImage(
            width,
            height,
            BufferedImage.TYPE_INT_ARGB
        );

        final var points = new ArrayList<Point>(numberOfPoints);
        final var random = new Random();

        for (int i = 0; i < numberOfPoints; i++) {
            points.add(
                new Point(random.nextInt(0, width), random.nextInt(0, height))
            );
        }

        final var start = System.nanoTime();

        for (int x = 0; x < width; x++) for (int y = 0; y < height; y++) {
            int minDist = Integer.MAX_VALUE;

            for (final var p : points)
                minDist = Math.min(minDist, p.squaredDistance(x, y));

            final var color =
                1.0F -
                Math.clamp((float) Math.sqrt(minDist), 0.0F, 255.0F) / 255.0F;

            image.setRGB(x, y, (new Color(color, color, color)).getRGB());
        }

        final var end = System.nanoTime();

        System.out.println(end - start);

        if (!saveImage) return;

        try {
            Files.createDirectories(Paths.get("img"));
            ImageIO.write(
                image,
                "png",
                new File("img/" + randomCharacters(10) + ".png")
            );
        } catch (final IOException e) {
            System.err.println(e.getMessage());
        }
    }

    private static final String characters =
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

    private static String randomCharacters(final int length) {
        final var builder = new StringBuilder(length);
        final var random = new Random();

        for (int i = 0; i < length; i++) builder.append(
            characters.charAt(random.nextInt(characters.length()))
        );

        return builder.toString();
    }
}
