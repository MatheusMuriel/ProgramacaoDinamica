memoria = {}

def calc(n):
    if n <= 1: return 1

    n_1 = 0
    n_2 = 0
    str_n1 = str(n-1)
    str_n2 = str(n-2)

    if (str_n1 in memoria):
      n_1 = memoria[str_n1]
    else:
      n_1 = calc(n-1)
      memoria[str_n1] = n_1

    if (str_n2 in memoria):
      n_2 = memoria[str_n2]
    else:
      n_2 = calc(n-2)
      memoria[str_n2] = n_2

    return n_1 + n_2

def get_funcao():
    return lambda n: calc(n)
