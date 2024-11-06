import runner_and_tournament
import runner
from runner_and_tournament import Tournament
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        mod = runner.Runner('Timur')
        for _ in range(10):
            mod.walk()
        self.assertEqual(mod.distance, 50)
    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        mod = runner.Runner('Timur')
        for _ in range(10):
            mod.run()
        self.assertEqual(mod.distance, 100)
    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        mod_1 = runner.Runner('Timur')
        mod_2 = runner.Runner('Denis')
        for _ in range(10):
            mod_1.walk()
            mod_2.run()
        self.assertNotEqual(mod_1.distance, mod_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def setUpClass(self):
        self.all_finishers = {}
        print(self.all_finishers)

    @classmethod
    def setUp(self):
        self.runer_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runer_2 = runner_and_tournament.Runner('Андрей', 9)
        self.runer_3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(self):
        for i in self.all_finishers:
            print(i)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def race_1_test(self):
        race_1 = runner_and_tournament.Tournament(90, self.runer_1, self.runer_3)
        result = race_1.start()
        print(result[list(result.keys())[-1]] == 'Ник')
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Error!')
        self.all_finishers[1] = result
        self.assertEqual(Tournament.start, 90)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def race_2_test(self):
        race_2 = runner_and_tournament.Tournament(90, self.runer_2, self.runer_3)
        result = race_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Error!')
        self.all_finishers[2] = result
        self.assertEqual(Tournament.start, 90)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def race_3_test(self):
        race_3 = runner_and_tournament.Tournament(90, self.runer_1, self.runer_2, self.runer_3)
        result = race_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Error!')
        self.all_finishers[3] = result
        self.assertEqual(Tournament.start, 90)

    if __name__ == "__main__":
        unittest.main()