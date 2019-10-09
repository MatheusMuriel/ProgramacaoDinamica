#sys.setrecursionlimit(1000000000)
class Fibonacci():

  def calc(self, n):
    if n == 0: return 0
    if n == 1: return 1

    return self.calc(n-1) + self.calc(n-2)

  def get_funcao_calc(self):
    return lambda n: self.calc(n)

  def __str__(self):
    return 'Recursivo puro'
