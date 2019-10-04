import time

from CommandLineInterface import Cli
from Resultado import Resultado
from fib_recursive import Fibonacci
from fib_rec_memorization import Memorization
from fib_iterativo_memorization import IterativoMemorization

def executa_algoritmo(nome_algoritmo, funcao_calc, inicio, fim):
    resultados = []
    
    for n in range(inicio, fim+1):
        tempo_inicial = time.process_time_ns()
    
        resultado_funcao = funcao_calc(n)

        tempo_final = time.process_time_ns()

        objeto_resultado = Resultado(tempo_inicial, tempo_final, nome_algoritmo, n, resultado_funcao)

        resultados.append(objeto_resultado)

    return resultados

codigos = {
    'Recursivo puro': Fibonacci(), 
    'Recursivo + Memoization': Memorization(), 
    'Iterativo + Memoization': IterativoMemorization()
    }

if __name__ == "__main__":
    parametros_execucao = Cli().get_dados()
    algoritmo = parametros_execucao[0]
    inicio = int(parametros_execucao[1])
    fim = int(parametros_execucao[2])

    funcao_calc = codigos[algoritmo].get_funcao_calc()

    resultados = executa_algoritmo(algoritmo, funcao_calc, inicio, fim)

    for resultado in resultados:
        print(resultado)
