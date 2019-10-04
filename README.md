### Benchmark de diferentes tipo de abordagens de programação dinamica

##### O foco do projeto é comparar a curva de eficiencia entre as diferentes abordagens em um calculo de numeros de Fibonacci

# Abordagens testadas:
- Puramente recursivo
- Recursivo + Memoization
- Iterativo + Memoization com limpeza de memoria
    
# Benchmark de cada abordagem:

### Especificações da maquina
    Sistema Operacional: Arch Linux
    Processador: Intel Core i5-6200U
    Memoria: 8GB RAM + 16GB de partição de Swap



## Puramente recursivo:
Devido ao limitador de recursão do Python o codigo acabou conseguindo calcular por volta de 40 numeros de Fibonacci

_Ainda não foi testado em um cenario sem a limitação de recurção._

## Recursivo + Memoization:
Testado em um cenario sem limite de recursão o codigo foi capaz de calcular até:

**16 889º** numero de Fibonacci em **0.034824 segundos**

Após isso o sistema operacional encera o processo por endereço invalido de memoria.

Ainda é necessario estudar mais afundo a causa do core dump do processo



## Iterativo + Memoization com limpeza de memoria:
Testado em um cenario sem limite de recursão e com uma memoria de 10 000 000 espaços e uma taxa de 30% a cada limpeza de memoria o codigo foi capaz de calcular até:

**400 000º** numero de Fibonacci

O benchmark interno do codigo contou 29.845317 segundos mas cronometrando o tempo em que a maquina ficou executando se passaram 3 minutos e 26,7 segundos

Ainda não se sabe se esse tempo foi devido ao tempo de execução do codigo ou a um travamento da maquina.

Com isso ainda não foi possivel concluir o tempo de execução do processo




# Bibliotecas usadas:
- MatplotLib
- PyInquirer
