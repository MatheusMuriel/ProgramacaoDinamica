from __future__ import print_function, unicode_literals
from PyInquirer import prompt, Separator, style_from_dict, Token
from pprint import pprint

def get_algoritmos(self):
    return ['Recursivo puro', 'Recursivo memorization', 'Iterativo memorization']


perguntas_execucao = [
    {
        'type': 'list',
        'name': 'tipo_teste',
        'message': 'Qual tipo de execução deseja testar?',
        'choices': [
            'Valor unitario',
            {
                'name': 'Range de valores',
                'disabled': 'Em desenvolvimento'
            }
        ]
    },
    {
        'type': 'list',
        'name': 'algoritmo',
        'message': 'Qual algoritmo deseja testar?',
        'choices': get_algoritmos,
    },
]

perguntas_teste_unitario = [
    {
        'type': 'input',
        'name': 'inicio',
        'message': 'Qual numero deseja?',
    }
]
perguntas_teste_range = [
    {
        'type': 'input',
        'name': 'inicio',
        'message': 'O ponto de inicio?',
    },
    {
        'type': 'input',
        'name': 'fim',
        'message': 'O ponto de fim?',
    }
]

def get_dados():
    respostas_1 = prompt(perguntas_execucao)
    respostas_2 = prompt(perguntas_teste_unitario) if respostas_1['tipo_teste'] == 'Valor unitario' else prompt(perguntas_teste_range)

    ALGORITMO = respostas_1['algoritmo']
    TIPO_TESTE = respostas_1['tipo_teste']
    INICIO = respostas_2['inicio']
    FIM = respostas_2['fim'] if 'fim' in respostas_2 else respostas_2['inicio'] 

    return (ALGORITMO, INICIO, FIM)