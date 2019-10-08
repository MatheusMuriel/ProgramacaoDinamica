import time
import sys

import Plotador
#from CommandLineInterface import Cli
from Resultado import Resultado
from fib_recursive import Fibonacci
from fib_rec_memorization import Memorization
from fib_iterativo_memorization import IterativoRecursiveMemorization
from fib_puramente_iterativo_memoization import IterativoMemorization

#sys.setrecursionlimit(1000000000)
def executa_algoritmo_bench(nome_algoritmo, funcao_calc, valor):

    tempo_inicial = time.time_ns()

    resultado_funcao = funcao_calc(valor)

    tempo_final = time.time_ns()

    return Resultado(tempo_inicial, tempo_final, nome_algoritmo, valor, resultado_funcao)

def executa_algoritmo(nome_algoritmo, funcao_calc, inicio, fim):
    resultados = []
    
    for n in range(inicio, fim+1):
        tempo_inicial = time.time_ns()
    
        resultado_funcao = funcao_calc(n)

        tempo_final = time.time_ns()

        objeto_resultado = Resultado(tempo_inicial, tempo_final, nome_algoritmo, n, resultado_funcao)

        resultados.append(objeto_resultado)

    return resultados

codigos = {
    'Recursivo puro': Fibonacci(), 
    'Recursivo + Memoization': Memorization(), 
    'Iterativo + Recursivo + Memoization': IterativoRecursiveMemorization(),
    'Iterativo puro + Memoization': IterativoMemorization()
    }

def modo_input_ususario():
    parametros_execucao = Cli().get_dados()
    algoritmo = parametros_execucao[0]
    inicio = int(parametros_execucao[1])
    fim = int(parametros_execucao[2])

    funcao_calc = codigos[algoritmo].get_funcao_calc()

    resultados = executa_algoritmo(algoritmo, funcao_calc, inicio, fim)

    for resultado in resultados:
        print(resultado)

    plot_eixo_x = list(map(lambda o: o.n, resultados))
    plot_eixo_y = list(map(lambda o: o.tempo_execucao, resultados))

    #Plotador.plot_simples(plot_eixo_x, plot_eixo_y, resultado.algoritimo)

def modo_benchmark():
    algoritmo = codigos['Iterativo puro + Memoization'].get_funcao_calc()
    inicio = 400000
    
    resultado = executa_algoritmo_bench('Iterativo puro + Memoization', algoritmo, inicio) 
    
    print (resultado)
    

if __name__ == "__main__":
    #modo_input_ususario()
    modo_benchmark()
    
