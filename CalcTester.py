import unittest
from calculator import Calculator
import sys

'''
    class for testing python calc

    reg = positive, neg, invalid, zero, None
    operation = invalid, zero, num

'''
class CalcTester(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_str_reg_none_op_none(self):
        """testing calculator oupt when register is None and operator is None"""
        self.calc.register = None
        self.calc.operation = None
        self.assertEqual(str(self.calc),'0') 
    def test_str_normal(self):
        """testing calculator oupt when register and operator are defined"""
        self.calc.register = 10
        self.calc.operation = '/'
        self.assertEqual(str(self.calc),'10 / ?') 
    def test_str__op_none(self):
        """testing calculator oupt when just operator is None"""
        self.calc.register = 18
        self.calc.operation = None
        self.assertEqual(str(self.calc),'18') 
    def test_str_reg_none(self):
        """testing calculator oupt when just register"""
        self.calc.register = None
        self.calc.operation = '*'
        self.assertEqual(str(self.calc),'0')
    @unittest.skipIf(sys.argv[0][-6:] == 'mut.py', "testing mutation")
    def test_str_reg_invalid_op_invalid(self):
        """testing calculator oupt when register is invalid and operator is invalid"""
        self.calc.register = "hello"
        self.calc.operation = "hello"
        self.assertEqual(str(self.calc),'error')
    @unittest.skipIf(sys.argv[0][-6:] == 'mut.py', "testing mutation")
    def test_str_reg_invalid(self):
        """testing calculator oupt when just register is invalid"""
        self.calc.register = "hello"
        self.calc.operation = "-"
        self.assertEqual(str(self.calc),'error')
    @unittest.skipIf(sys.argv[0][-6:] == 'mut.py', "testing mutation")
    def test_str_op_invalid(self):
        """testing calculator oupt when just operator is invalid"""
        self.calc.register = -5
        self.calc.operation = "hello"
        self.assertEqual(str(self.calc),'error')

    def test_set_op_reg_none(self):
        """testing set_op when register is None"""
        self.calc.register = None
        self.calc.operation = "*"
        self.calc.set_op('/')
        self.assertEqual(self.calc.operation, '*')
    def test_set_op(self):
        """testing set_op when register is number"""
        self.calc.register = 10
        self.calc.operation = "*"
        self.calc.set_op('/')
        self.assertEqual(self.calc.operation, '/')
    def test_set_op_invalid(self):
        """testing set_op when operator is None"""
        self.calc.operation = "*"
        self.calc.set_op(None)
        self.assertEqual(self.calc.operation, '*')


    def test_eval_plus(self):
        """testing evlaution with addition"""
        self.calc.register = 8
        self.calc.operation = '+'
        self.assertEqual(self.calc.evaluate(2), 10)
    def test_eval_minus(self):
        """testing evlaution with subtraction"""
        self.calc.register = 8
        self.calc.operation = '-'
        self.assertEqual(self.calc.evaluate(2), 6)
    def test_eval_divide(self):
        """testing evlaution with division"""
        self.calc.register = 8
        self.calc.operation = '/'
        self.assertEqual(self.calc.evaluate(2), 4)

    @unittest.skipIf(sys.argv[0][-6:] == 'mut.py', "testing mutation")
    def test_eval_mod(self):
        """testing evlaution with modulo"""
        self.calc.register = 8
        self.calc.operation = '%'
        self.assertEqual(self.calc.evaluate(2), 0)
    def test_eval_times(self):
        """testing evlaution with multiplication"""
        self.calc.register = 8
        self.calc.operation = '*'
        self.assertEqual(self.calc.evaluate(2), 16)
    def test_eval_invalid_type(self):
        """testing evlaution with invalid input"""
        self.calc.register = 8
        self.calc.operation = '+'
        self.assertRaises(TypeError, self.calc.evaluate, "hello")
    def test_eval_invalid_key(self):
        """testing evlaution with invalid key"""
        self.calc.register = 8
        self.calc.operation = 'error'
        self.assertRaises(KeyError, self.calc.evaluate, 5)

    def test_set_number(self):
        """Testing set number when register is number"""
        self.calc.register = -15
        self.calc.operation = "*"
        self.calc.set_number(-2.5)
        self.assertEqual(self.calc.register, 37.5)
    def test_set_number_reg_none(self):
        """Testing set number when register is None"""
        self.calc.register = None
        self.calc.operation = "*"
        self.calc.set_number(-2.5)
        self.assertEqual(self.calc.register, -2.5)

    def test_clear(self):
        """testing clear register"""
        self.calc.register = -15
        self.calc.clear()
        self.assertEqual(self.calc.register, None)

    def mainLoop(self, x):
        if x == '':
            self.calc.clear()
        else:
            try:
                self.calc.set_number(float(x))
            except Exception as e:
                self.calc.set_op(x)
        return str(self.calc)

    def test_main_add(self):
        """testing main loop with addition"""
        self.mainLoop('10.07')
        self.mainLoop('+')
        self.mainLoop('-12.3344')
        self.mainLoop('+')
        self.assertEqual(self.mainLoop('14.3'), str(10.07+-12.3344+14.3))
    def test_main_sub(self):
        """testing main loop with subtraction"""
        self.mainLoop('-300')
        self.mainLoop('-')
        self.mainLoop('-33.666')
        self.mainLoop('-')
        self.assertEqual(self.mainLoop('66'), str(-300--33.666-66))
    def test_main_mult(self):
        """testing main loop with multiplication"""
        self.mainLoop('-30.0')
        self.mainLoop('*')
        self.mainLoop('53.2')
        self.mainLoop('*')
        self.assertEqual(self.mainLoop('66'), str(-30*53.2*66))
    def test_main_divide(self):
        """testing main loop with division"""
        self.mainLoop('-44')
        self.mainLoop('/')
        self.mainLoop('69')
        self.mainLoop('/')
        self.assertEqual(self.mainLoop('-2'), str(-44 / 69 / -2))
    @unittest.skipIf(sys.argv[0][-6:] == 'mut.py', "testing mutation")
    def test_main_mod(self):
        """testing main loop with modulo"""
        self.mainLoop('-30')
        self.mainLoop('%')
        self.mainLoop('53')
        self.mainLoop('%')
        self.assertEqual(self.mainLoop('4'), str(-30%53%4))
    @unittest.skipIf(sys.argv[0][-6:] == 'mut.py', "testing mutation")
    def test_main_mix(self):
        """testing main loop with mix of arithmetic"""
        self.mainLoop('-30')
        self.mainLoop('%')
        self.mainLoop('53')
        self.mainLoop('*')
        self.mainLoop('2.056')
        self.mainLoop('/')
        self.mainLoop('-55.34')
        self.mainLoop('-')
        self.mainLoop('300.11')
        self.mainLoop('+')
        self.assertEqual(self.mainLoop('4'),
                         str(-30 % 53 * 2.056 / -55.34 - 300.11 + 4))
    @unittest.skipIf(sys.argv[0][-6:] == 'mut.py', "testing mutation")
    def test_main_invalid(self):
        """testing main loop with invalid input"""
        self.mainLoop('30')
        self.assertEqual(self.mainLoop('error'), 'error')

if __name__ == '__main__':
    unittest.main()