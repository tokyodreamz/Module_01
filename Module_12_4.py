class Runner:
    def __init__(self, name, speed):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if speed < 0:
            raise ValueError("Speed cannot be negative")
        self.name = name
        self.speed = speed

    def walk(self):
        return f"{self.name} is walking at speed {self.speed}"

    def run(self):
        return f"{self.name} is running at speed {self.speed}"


import logging
import unittest
from test_12_4 import Runner


logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("John", -5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner = Runner(123, 10)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")

if __name__ == '__main__':
    unittest.main()