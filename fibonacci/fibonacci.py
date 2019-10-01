import sys

def fib(n):
    if n <= 1: return 1
    return fib(n-1) + fib(n-2)


n = 0
if len(sys.argv) == 1:
    print('Deseja calcular até qual numero?')
    n = int(input('> '))
else:
    n = int(sys.argv[1])

print('Resultado: ', fib(n))


