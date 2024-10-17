class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return (len(new_sides) == len(self.__sides) and
                all(isinstance(side, int) and side > 0 for side in new_sides))

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * 3.141592653589793)

    def get_square(self):
        return 3.141592653589793 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1:
            sides = [1]
        super().__init__(color, *sides * self.sides_count)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3


# Код проверки:
circle1 = Circle((200, 200, 100), 10)  # (Color, Sides)
cube1 = Cube((222, 35, 130), 6)

# Проверка изменение цветов:
circle1.set_color(55, 66, 77)  # Yes
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # No
print(cube1.get_color())

# Проверка изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # No
print(cube1.get_sides())
circle1.set_sides(15)  # Yes
print(circle1.get_sides())

# Проверка периметра (круга) = длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())