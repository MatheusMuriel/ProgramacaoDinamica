def calc(n):
    if n == 0: return 0
    if n == 1: return 1

    return calc(n-1) + calc(n-2)

def reset():
  pass

def get_funcao_calc():
    return lambda n: calc(n)

def get_funcao_reset():
    return lambda: reset()
