import gc
class Memorization():
  def __init__(self):
    LIMITE = 10000000
    TAXA_LIMPEZA = 0.7
    self.memoria = Memoria(LIMITE, TAXA_LIMPEZA)

  # @profile
  def calc(self, n):
      if n == 0: return 0
      if n == 1: return 1

      str_n1 = str(n-1)
      str_n2 = str(n-2)
      n_1 = self.memoria.get_lembranca(str_n1)
      n_2 = self.memoria.get_lembranca(str_n2)

      if (n_1 == -1):
        n_1 = self.calc(n-1)
        self.memoria.nova_memoria(str_n1, n_1)

      if (n_2 == -1):
        n_2 = self.calc(n-2)
        self.memoria.nova_memoria(str_n2, n_2)
      
      return n_1 + n_2

  def get_funcao_calc(self):
      return lambda n: self.calc(n)

  def get_funcao_reset(self):
      return lambda: self.reset()
