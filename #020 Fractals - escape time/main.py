from PIL import Image, ImageDraw

WIDTH = 1000
HEIGHT = 700
START_X = -2
END_X = 1
START_Y = -1
END_Y = 1

MAX_ITERATIONS = 255


def main():
    im = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # transform from pixel coordinate to complex coordinate
            a, b = transform_x(x), transform_y(y)
            c = complex(a, b)
            iterations = mandelbrot(c)
            hue = int(iterations * 255 / MAX_ITERATIONS)
            saturation = 255
            value = 255 if iterations < MAX_ITERATIONS else 0
            draw.point([x, y], (hue, saturation, value))
    im.convert('RGB')
    im.show()


def transform_x(x):
    return (x / WIDTH) * (END_X - START_X) + START_X


def transform_y(y):
    return (y / HEIGHT) * (END_Y - START_Y) + START_Y


def mandelbrot(c):
    z = 0
    iterations = 0
    while iterations < MAX_ITERATIONS and abs(z) <= 2:
        z = z * z + c
        iterations += 1
    return iterations


if __name__ == '__main__':
    main()
