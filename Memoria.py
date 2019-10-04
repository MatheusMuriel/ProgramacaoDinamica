
class Cerebro():

  def __init__(self, limite, taxa_de_limpeza):
    self.memoria = {}
    self.usos = {}
    self.limite = limite
    self.taxa_de_limpeza = taxa_de_limpeza

  def nova_memoria(self, nome, valor):
    if (len(self.memoria) >= self.limite):
      self.limpar_memoria()
    self.memoria[nome] = valor
    self.usos[nome] = 1

  def get_lembranca(self, nome):
    if (nome in self.memoria):
      self.usos[nome] += 1
      return self.memoria[nome]
    else:
      return -1

  def limpar_memoria(self):
    while(len(self.memoria) > self.limite*(self.taxa_de_limpeza)):
      self.memoria.pop(min(self.memoria.items())[0])