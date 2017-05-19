from CalcTester import CalcTester
from path1 import Path1
import unittest


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suites = []
    suites.append(loader.loadTestsFromTestCase(Path1))
    suites.append(loader.loadTestsFromTestCase(CalcTester))

    big_suite = unittest.TestSuite(suites)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)

