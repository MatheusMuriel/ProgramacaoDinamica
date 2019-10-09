import Memoria as memo

#sys.setrecursionlimit(1000000000)

class IterativoRecursiveMemorization():
  def __init__(self):
    LIMITE = 4000000
    TAXA_LIMPEZA = 0.7
    self.memoria = memo.Cerebro(LIMITE, TAXA_LIMPEZA)

  def calcular(self, n):
    valor_final = 0

    for i in range(2, n+1):
      str_n1 = str(i-1)
      str_n2 = str(i-2)
      str_n3 = str((i-1)+(i-2))
      n_1 = self.memoria.get_lembranca(str_n1)
      n_2 = self.memoria.get_lembranca(str_n2)

      if (n_1 == -1 and (i-1) > 1):
        n_1 = self.calc_fib(i-1)
        #print("fib({})={}".format(str_n1, n_1))
        self.memoria.nova_memoria(str_n1, n_1)

      elif (n_2 == -1 and (i-2) > 1):
        n_2 = self.calc_fib(i-2)
        self.memoria.nova_memoria(str_n2, n_2)

      if( i > 3):
        n_3 = n_1 + n_2
        #print ("FIB({}) :: fib({})={} + fib({})={}     = {}".format(str_n3, (i-1), n_1, (i-2), n_2, n_3))
        self.memoria.nova_memoria(i, n_3)
        valor_final = n_3

    return valor_final

  def calc_fib(self, n):
      if n == 0: return 0
      if n == 1: return 1

      str_n1 = str(n-1)
      str_n2 = str(n-2)
      n_1 = self.memoria.get_lembranca(str_n1)
      n_2 = self.memoria.get_lembranca(str_n2)

      if (n_1 == -1):
        n_1 = self.calc_fib(n-1)
        self.memoria.nova_memoria(str_n1, n_1)

      if (n_2 == -1):
        n_2 = self.calc_fib(n-2)
        self.memoria.nova_memoria(str_n2, n_2)
      
      return n_1 + n_2

  def get_funcao_calc(self):
      return lambda n: self.calcular(n)

  def __str__(self):
    return 'Iterativo + Recursivo + Memoization'