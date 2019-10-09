import time
import sys

#from CommandLineInterface import Cli
import cli
from Resultado import Resultado
from fib_recursive import Fibonacci
from fib_rec_memorization import Memorization
from fib_iterativo_memorization import IterativoRecursiveMemorization
from fib_puramente_iterativo_memoization import IterativoMemorization

testes = ["Range de valores", "Valor unitario"]
algoritmos = [Fibonacci(), Memorization(), IterativoRecursiveMemorization(), IterativoMemorization()]

def executa_algoritmo(nome_algoritmo, funcao_calc, inicio, fim):
    resultados = []
    
    for n in range(inicio, fim+1):
        tempo_inicial = time.time_ns()
    
        resultado_funcao = funcao_calc(n)

        tempo_final = time.time_ns()

        objeto_resultado = Resultado(tempo_inicial, tempo_final, nome_algoritmo, n, resultado_funcao)

        resultados.append(objeto_resultado)

    return resultados

def modo_input_ususario():
    cli.setar_opcoes(testes, algoritmos)
    
    dict_respostas = cli.get_respostas()
    algoritmo = dict_respostas["algoritmo"]
    valor = dict_respostas["valor"]

    funcao_calc = algoritmo.get_funcao_calc()

    resultados = executa_algoritmo(algoritmo, funcao_calc, valor, valor)

    for resultado in resultados:
        print(resultado)

    #plot_eixo_x = list(map(lambda o: o.n, resultados))
    #plot_eixo_y = list(map(lambda o: o.tempo_execucao, resultados))
    #Plotador.plot_simples(plot_eixo_x, plot_eixo_y, resultado.algoritimo)
    
if __name__ == "__main__":
    modo_input_ususario()
    
