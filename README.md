### Benchmark de diferentes tipo de abordagens de programação dinamica para calcular um numero de Fibonacci

Projeto feito apenas com Python 3.7 puro.

Recorde atual: **Fibonacci(998000)**

# Como testar: 
Existem 2 modos de executar:
- Modo input de usuario
- Modo Benchmark

Modo de input de usuario:
O usuario escolhe qual algoritmo e qual o valor a calcular
````
~$ python main.py
````

Modo de input de Benchmark:
O algoritmo e o valor a calcular são definidos diretamente no arquivo benchmark.py
````
~$ python benchmark.py
````

# Abordagens testadas:
- Puramente recursivo
- Recursivo + Memoization
- Iterativo + Recursivo + Memoization
- Iterativo puro + Memoization
    
# Benchmark de cada abordagem:

### Especificações da maquina
    Sistema Operacional: Arch Linux
    Processador: Intel Core i5-6200U
    Memoria: 8GB RAM + 16GB de partição de Swap

____

## Puramente recursivo:
Devido ao limitador de recursão do Python o codigo acabou conseguindo calcular por volta de 40 numeros de Fibonacci

_Ainda não foi testado em um cenario sem a limitação de recurção._

____

## Recursivo + Memoization:
Testado em um cenario sem limite de recursão o codigo foi capaz de calcular até:

**16 889º** numero de Fibonacci em **0.034824 segundos**

Após isso o sistema operacional encera o processo por endereço invalido de memoria.

Ainda é necessario estudar mais afundo a causa do core dump do processo

____

## Iterativo + Recursivo + Memoization:
Testado em um cenario sem limite de recursão e com uma memoria de 10 000 000 espaços e uma taxa de 30% a cada limpeza de memoria o codigo foi capaz de calcular até:

**500 000º** numero de Fibonacci

Em um tempo de 3 minutos e 19,6 segundos
____

## Iterativo puro + Memoization:
Nesse caso não foi preciso alterar o limite de recursão, e em um cenario sem limite de tamanho para o Memoization o algoritmo foi capaz de calcular até

**500 000º** numero de Fibonacci

em um tempo de **96 segundos**

Foi visto que o limite de execução e a velocidade está relacionado a quantidade de memoria disponivel

Em uma maquina com 16GB de RAM o mesmo algoritmo foi capaz de calcular até:

**998 000º** numero de Fibonacci em **117 segundos**

A velocidade de execução do algoritmo começa a diminuir bruscamente quando a memoria do computador começa a utilizar swap em disco