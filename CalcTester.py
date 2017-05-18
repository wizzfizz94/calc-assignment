import unittest
from calculator import Calculator

'''
    class for testing python calc

    reg = positive, neg, invalid, zero, None
    operation = invalid, zero, num

'''
class CalcTester(unittest.TestCase):

    def setUp(self):
        self.calcs = []
        self.reg_vals = [12.54, -12.54, None, 'hello', '0']
        self.op_vals = ['*', None, 'hello']
        for reg in self.reg_vals:
            for op in self.op_vals:
                c = Calculator()
                c.register = reg
                c.operation = op
                self.calcs.append(c)

    def test_str_reg_none_op_none(self):
        self.calc.register = None
        self.calc.operation = None 
    def test_str_normal(self):
        self.calc.register = 10
        self.calc.operation = '/' 
    def test_str__op_none(self):
        self.calc.register = 18
        self.calc.operation = None 
    def test_str_reg_none(self):
        self.calc.register = None
        self.calc.operation = '*' 
    def test_str_reg_invalid_op_invalid(self):
        self.calc.register = "hello"
        self.calc.operation = "hello" 
    def test_str_reg_invalid(self):
        self.calc.register = "hello"
        self.calc.operation = "" 
    def test_str_op_invalid(self):
        self.calc.register = None
        self.calc.operation = "hello" 






if __name__ == '__main__':
    unittest.main()