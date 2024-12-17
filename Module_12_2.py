class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __eq__(self, other):
        return self.name == other.name


class Tournament:
    def __init__(self, distance, runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        results = {}
        times = {}

        for runner in self.runners:
            time_to_finish = self.distance / runner.speed
            times[runner] = time_to_finish

        sorted_runners = sorted(times, key=times.get)

        for position, runner in enumerate(sorted_runners, start=1):
            results[position] = runner

        return results


import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner("Усэйн", 10)
        self.runner_andrey = Runner("Андрей", 9)
        self.runner_nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value.name}")

    def test_usain_and_nick(self):
        tournament = Tournament(90, [self.runner_usain, self.runner_nick])
        results = tournament.start()
        self.__class__.all_results[1] = results
        self.assertTrue(results[max(results)].name == "Ник")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, [self.runner_andrey, self.runner_nick])
        results = tournament.start()
        self.__class__.all_results[2] = results
        self.assertTrue(results[max(results)].name == "Ник")

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, [self.runner_usain, self.runner_andrey, self.runner_nick])
        results = tournament.start()
        self.__class__.all_results[3] = results
        self.assertTrue(results[max(results)].name == "Ник")


if __name__ == '__main__':
    unittest.main()