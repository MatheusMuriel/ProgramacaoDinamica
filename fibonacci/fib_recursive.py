def calc(n):
    if n <= 1: return 1
    return calc(n-1) + calc(n-2)

def get_funcao():
    return lambda n: calc(n)
