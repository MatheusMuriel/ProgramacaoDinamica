import sys
import datetime
import fib_recursive
import Resultado

argumentos = sys.argv
algoritimos = ['Recursivo']

def pega_algoritmo():
    print('Escolha um algoritmo: ')
    for alg in algoritimos:
        index = algoritimos.index(alg)
        print(index, ': ', alg)
    return int(input('> '))

def pega_numero():
    print('Deseja calcular até qual numero?')
    return int(input('> '))

def executa_algoritmo(nome_algoritmo, funcao, n):
    tempo_inicial = datetime.datetime.now()

    resultado = funcao(n)

    tempo_final = datetime.datetime.now()

    return Resultado.Resultado(tempo_final, tempo_final, nome_algoritmo, n, resultado)


algoritimo = int(argumentos[1]) if len(argumentos) >= 2 else pega_algoritmo()
n = int(argumentos[2]) if len(argumentos) >= 3 else pega_numero()

funcao = None
if algoritimo == 0:
    funcao = fib_recursive.get_funcao()

resultado = executa_algoritmo(algoritimos[algoritimo], funcao, n)

print(resultado)
