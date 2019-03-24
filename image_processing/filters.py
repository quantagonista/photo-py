import threading

from PIL import Image

from image_processing.utils import get_empty_matrix


class BaseFilter:
    name = 'Base Filter'
    radius = 1

    def apply(self) -> Image.Image:
        raise NotImplementedError


class MatrixFilter(BaseFilter):
    name = 'Base Matrix Filter'
    matrix = None

    def __init__(self, image: Image.Image, radius=1):
        self.image = image
        self.radius = radius
        self.divisor = self.get_divisor()

        self.width = image.width
        self.height = image.height

        size = (self.width, self.height)
        self.red = get_empty_matrix(*size)
        self.green = get_empty_matrix(*size)
        self.blue = get_empty_matrix(*size)

        self.new_red = get_empty_matrix(*size)
        self.new_green = get_empty_matrix(*size)
        self.new_blue = get_empty_matrix(*size)

    def apply(self):
        self.prepare_channels()
        return self.process_channels()

    def get_divisor(self):
        return 1 / sum(sum(row) for row in self.matrix)

    def prepare_channels(self):
        for y in range(self.height):
            for x in range(self.width):
                pixel = self.image.getpixel(xy=(x, y))
                self.red[y][x] = pixel[0]
                self.green[y][x] = pixel[1]
                self.blue[y][x] = pixel[2]

    def process_channels(self):
        red_thread = threading.Thread(target=self.process_channel, args=(self.red, self.new_red))
        blue_thread = threading.Thread(target=self.process_channel, args=(self.blue, self.new_blue))
        green_thread = threading.Thread(target=self.process_channel, args=(self.green, self.new_green))

        red_thread.start()
        blue_thread.start()
        green_thread.start()

        red_thread.join()
        blue_thread.join()
        green_thread.join()

        return self.build_new_image()

    def process_channel(self, input_channel, output_channel):
        for y in range(self.radius, self.height - self.radius):
            for x in range(self.radius, self.width - self.radius):
                pixel_neighbourhood = self.get_pixel_neighbourhood(x, y, input_channel)
                new_value = self.calculate_pixel_value(pixel_neighbourhood)
                output_channel[y][x] = new_value

    def get_pixel_neighbourhood(self, x, y, channel, radius=None):
        if not radius:
            radius = self.radius

        start = (x - radius, y - radius)
        end = (x + radius, y + radius)
        size = 2 * radius + 1

        neighbourhood = get_empty_matrix(size, size)

        ny = 0
        for y in range(start[1], end[1] + 1):
            nx = 0

            for x in range(start[0], end[0] + 1):
                neighbourhood[ny][nx] = channel[y][x]
                nx += 1
            ny += 1

        return neighbourhood

    def build_new_image(self):
        image = Image.new('RGB', (self.width, self.height))
        for y in range(self.height):
            for x in range(self.width):
                pixel = (self.new_red[y][x], self.new_green[y][x], self.new_blue[y][x],)
                image.putpixel((x, y), pixel)
        return image

    def calculate_pixel_value(self, neighbourhood):
        new_value = 0
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                pixel_value = neighbourhood[y][x]
                matrix_value = self.matrix[y][x]
                new_value = new_value + pixel_value * matrix_value * self.divisor % 255
                new_value = int(new_value)
        return new_value


class FastBlur(MatrixFilter):
    matrix = [
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1],
    ]
