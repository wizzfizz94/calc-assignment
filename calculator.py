
class Calculator():

  '''One register with number and an operation...'''


  def __init__(self):
    self.register = None
    self.operation = None

  def __str__(self):
    s = '0'
    if self.register!=None:
      s = str(self.register)
      if self.operation!=None:
        s += ' '+self.operation+' ?'
    return s

  def set_op(self, op):
    if self.register != None:
      self.operation = op

  def evaluate(self, num):
     ops =  {'+' : lambda x: self.register + x, 
         '-' : lambda x: self.register - x, 
         '/' : lambda x: self.register / x,
         '*' : lambda x: self.register * x}
     return ops[self.operation](num)

  def set_number(self,num):
    try:
     if self.register == None:
      self.register = num
     else:
      self.register = self.evaluate(num)
      self.operation = None
    except Exception as e:
      print(e)


  def clear(self):
    self.register = None


if __name__ == '__main__':
  calc = Calculator()
  while True:
    x = input()
    if x=='':
      calc.clear()
    else:  
      try:
        calc.set_number(float(x))
      except Exception as e:
        calc.set_op(x)
    print(calc)


