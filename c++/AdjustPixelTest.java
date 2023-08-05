import java.io.*;
import java.util.*;

// Pixel.java
class Pixel {
    private int red;
    private int green;
    private int blue;

    // Constructor
    public Pixel(int red, int green, int blue) {
        this.red = red;
        this.green = green;
        this.blue = blue;
    }

    // Getters and setters for each component
    public int getRed() {
        return red;
    }

    public void setRed(int red) {
        this.red = red;
    }

    public int getGreen() {
        return green;
    }

    public void setGreen(int green) {
        this.green = green;
    }

    public int getBlue() {
        return blue;
    }

    public void setBlue(int blue) {
        this.blue = blue;
    }
}

// TransformablePicture.java 
class TransformablePicture {
    private Pixel[][] pixels;

    // Constructor and other methods for TransformablePicture
    // ...

    // Implementing adjustPixel() method
    public void adjustPixel(Pixel pixel, int amount) {
        pixel.setRed(pixel.getRed() + amount);
        pixel.setGreen(pixel.getGreen() + amount);
        pixel.setBlue(pixel.getBlue() + amount);
    }
}

// Test case for adjustPixel()
public class AdjustPixelTest {
    public static void main(String[] args) {
        // Create a sample pixel with RGB values (100, 150, 200)
        Pixel testPixel = new Pixel(100, 150, 200);

        // Create a TransformablePicture object
        TransformablePicture picture = new TransformablePicture();

        // Print the original pixel values
        System.out.println("Original Pixel: R=" + testPixel.getRed() + ", G=" + testPixel.getGreen() + ", B=" + testPixel.getBlue());

        // Adjust the pixel by adding 50 to each RGB component
        picture.adjustPixel(testPixel, 50);

        // Print the updated pixel values
        System.out.println("Adjusted Pixel: R=" + testPixel.getRed() + ", G=" + testPixel.getGreen() + ", B=" + testPixel.getBlue());
    }
}
