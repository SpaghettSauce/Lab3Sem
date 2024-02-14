from PIL import Image

def invert_brightness(image_path):
    image = Image.open(image_path)
    pixels = image.load()
    image.show()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            in_r = 255 - r
            in_g = 255 - g
            in_b = 255 - b
            pixels[x, y] = (in_r, in_g, in_b)
    image.show()

image_path = "garf.jpg"
inverted_image_path = invert_brightness(image_path)