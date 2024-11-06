import unittest
import module_12_3

tes = unittest.TestSuite()
tes.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3.RunnerTest))
tes.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tes)