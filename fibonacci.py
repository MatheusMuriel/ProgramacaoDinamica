import sys
import datetime
import time
import fib_recursive
import Resultado
import Plotador
import fib_rec_memorization
import fib_iterativo_memorization
import resource

sys.setrecursionlimit(1000000000)
sys.settrace
resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
resource.setrlimit(resource.RLIMIT_MEMLOCK, (0, 0))

argumentos = sys.argv
algoritimos = ['Recursivo puro', 'Recursivo memorization', 'Iterativo memorization']

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

# @profile
def executa_algoritmo(nome_algoritmo, funcao_calc, inicio, fim):
    resultados = []
    
    for n in range(inicio, fim+1):
        tempo_inicial = time.process_time_ns()
    
        resultado_funcao = funcao_calc(n)

        tempo_final = time.process_time_ns()

        objeto_resultado = Resultado.Resultado(tempo_inicial, tempo_final, nome_algoritmo, n, resultado_funcao)

        resultados.append(objeto_resultado)

    return resultados

if (argumentos[1] != 'auto'):

    #memorization = fib_rec_memorization.Memorization()
    it_memo = fib_iterativo_memorization.IterativoMemorization()

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

    funcao_calc = None
    funcao_reset = None
    if algoritimo == 0:
        funcao_calc = fib_recursive.get_funcao_calc()
    elif (algoritimo == 1):
        funcao_calc = None
    elif (algoritimo == 2):
        funcao_calc = it_memo.get_funcao_calc()

    resultados = executa_algoritmo(algoritimos[algoritimo], funcao_calc, inicio, fim)

    for resultado in resultados:
        print(resultado)

    #result_plot_x = list(map(lambda o: o.n, resultados))
    #result_plot_y = list(map(lambda o: o.get_tempo(), resultados))

    #if (len(resultados) > 1):
        #Plotador.plot_simples(result_plot_x, result_plot_y, algoritimos[algoritimo])

else: 
    
    memorization = fib_rec_memorization.Memorization()

    inicio = 22
    fim = 40
    
    func_rec = fib_recursive.get_funcao_calc()
    func_rec_reset = fib_recursive.get_funcao_reset()
    func_memo = memorization.get_funcao_calc()
    func_memo_reset = memorization.get_funcao_reset()

    result_rec = executa_algoritmo(algoritimos[0], func_rec, func_rec_reset, inicio, fim)
    result_memo = executa_algoritmo(algoritimos[1], func_memo, func_memo_reset, inicio, fim)

    #for i in range (0, len(result_memo)-1):
        #print(result_rec[i])
        #print(result_memo[i])

    get_n = lambda o: o.n
    get_tempo = lambda o: o.get_tempo()

    result_plot_x1 = list(map(get_n, result_rec ))
    result_plot_y1 = list(map(get_tempo, result_rec))

    result_plot_x2 = list(map(get_n, result_memo))
    result_plot_y2 = list(map(get_tempo, result_memo))

    Plotador.plot_duplo(inicio, fim, result_plot_y2, 'Recursivo Puro', result_plot_y1, 'Memorization')