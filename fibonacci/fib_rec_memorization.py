
class Memorization():
  def __init__(self):
    self.memoria = {}

  def calc(self, n):
      if n <= 1: return 1

      n_1 = 0
      n_2 = 0
      str_n1 = str(n-1)
      str_n2 = str(n-2)

      if (str_n1 in self.memoria):
        n_1 = self.memoria[str_n1]
      else:
        n_1 = self.calc(n-1)
        self.memoria[str_n1] = n_1

      if (str_n2 in self.memoria):
        n_2 = self.memoria[str_n2]
      else:
        n_2 = self.calc(n-2)
        self.memoria[str_n2] = n_2

      return n_1 + n_2

  def reset(self):
    self.memoria = {}

  def get_funcao_calc(self):
      return lambda n: self.calc(n)

  def get_funcao_reset(self):
      return lambda: self.reset()
