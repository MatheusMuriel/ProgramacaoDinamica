import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def plot(x, y):

  # Data for plotting
  xx = np.array(x)
  yy = np.array(y)

  fig, ax = plt.subplots()
  ax.plot(xx, yy)

  ax.set(xlabel='Tamanho N', ylabel='Tempo de execução',
        title='Fibonacci Recursivo Puro')
  ax.grid()

  fig.savefig("FibRec.png")
  plt.show()