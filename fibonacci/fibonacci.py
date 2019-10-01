import sys
import datetime
import time
import fib_recursive
import Resultado
import Plotador

argumentos = sys.argv
algoritimos = ['Recursivo']

def pega_algoritmo():
    print('Escolha um algoritmo: ')
    for alg in algoritimos:
        index = algoritimos.index(alg)
        print(index, ': ', alg)
    return int(input('> '))

def pega_numero(mensagem=''):
    print('Deseja qual numero?' if mensagem == '' else mensagem)
    return int(input('> '))

def pega_tipo_teste():
    print('Deseja testar unitariamente ou em um range?')
    print('0 - Unitario')
    print('1 - Range')
    return int(input('> '))

def executa_algoritmo(nome_algoritmo, funcao, inicio, fim):
    resultados = []

    for n in range(inicio, fim+1):
        tempo_inicial = time.process_time_ns()

        resultado_funcao = funcao(n)

        tempo_final = time.process_time_ns()

        objeto_resultado = Resultado.Resultado(tempo_inicial, tempo_final, nome_algoritmo, n, resultado_funcao)
        resultados.append(objeto_resultado)

    return resultados

algoritimo = int(argumentos[1]) if len(argumentos) >= 2 else pega_algoritmo()
tipo_teste = int(argumentos[2]) if len(argumentos) >= 3 else pega_tipo_teste()

inicio, fim = 0, 0
if (tipo_teste == 0):
    n = int(argumentos[3]) if len(argumentos) >= 4 else pega_numero()
    inicio, fim = n, n
elif (tipo_teste == 1):
    #inicio = pega_numero(mensagem='Inicio')
    inicio = int(argumentos[3]) if len(argumentos) >= 4 else pega_numero(mensagem='Inicio')
    #fim = pega_numero(mensagem='Fim')
    fim = int(argumentos[4]) if len(argumentos) >= 5 else pega_numero(mensagem='Fim')

funcao = None
if algoritimo == 0:
    funcao = fib_recursive.get_funcao()
elif (algoritimo == 1):
    pass

resultados = executa_algoritmo(algoritimos[algoritimo], funcao, inicio, fim)

for resultado in resultados:
    print(resultado)

result_plot_x = list(map(lambda o: o.n, resultados))
result_plot_y = list(map(lambda o: o.tempo_execucao, resultados))

print(result_plot_x)
print(result_plot_y)

Plotador.plot(result_plot_x, result_plot_y)