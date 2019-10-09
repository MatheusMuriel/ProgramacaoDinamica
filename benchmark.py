import time
import sys

from Resultado import Resultado
from fib_recursive import Fibonacci
from fib_rec_memorization import Memorization
from fib_iterativo_memorization import IterativoRecursiveMemorization
from fib_puramente_iterativo_memoization import IterativoMemorization

def executa_algoritmo_bench(nome_algoritmo, funcao_calc, valor):

    tempo_inicial = time.time_ns()

    resultado_funcao = funcao_calc(valor)

    tempo_final = time.time_ns()

    return Resultado(tempo_inicial, tempo_final, nome_algoritmo, valor, resultado_funcao)

def modo_benchmark():
    codigo = IterativoMemorization()
    algoritmo = codigo.get_funcao_calc()
    valor = 100000
    
    resultado = executa_algoritmo_bench(codigo, algoritmo, valor) 
    
    print (resultado)

    detalhes_execucao = "\nFib({})\nAlgoritmo :: {}".format(valor, codigo)
    print(detalhes_execucao)

    
if __name__ == "__main__":
    modo_benchmark()
    
