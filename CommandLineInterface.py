from __future__ import print_function, unicode_literals
from PyInquirer import prompt, Separator, style_from_dict, Token
from pprint import pprint

class Cli():

    def __init__(self):
        self.algoritmos = ['Recursivo puro', 'Recursivo + Memoization', 'Iterativo + Memoization']

        self.perguntas_execucao = [
            {
                'type': 'list',
                'name': 'tipo_teste',
                'message': 'Qual tipo de execução deseja testar?',
                'choices': [
                    'Valor unitario',
                    {
                        'name': 'Range de valores',
                        #'disabled': 'Em desenvolvimento'
                    }
                ]
            },
            {
                'type': 'list',
                'name': 'algoritmo',
                'message': 'Qual algoritmo deseja testar?',
                'choices': self.algoritmos,
            },
        ]
        self.perguntas_teste_unitario = [
            {
                'type': 'input',
                'name': 'inicio',
                'message': 'Qual numero deseja?',
                'validate': lambda val: val.isnumeric() and int(val) >=0 or 'Informe um valor numerico maior ou igual a 0'
            }
        ]
        self.perguntas_teste_range = [
            {
                'type': 'input',
                'name': 'inicio',
                'message': 'O ponto de inicio?',
                'validate': lambda val: val.isnumeric() and int(val) >=0 or 'Informe um valor numerico maior ou igual a 0'
            },
            {
                'type': 'input',
                'name': 'fim',
                'message': 'O ponto de fim?',
                'validate': lambda val: val.isnumeric() and int(val) >=0 or 'Informe um valor numerico maior ou igual a 0'
            }
        ]

    def get_dados(self):
        respostas_1 = prompt(self.perguntas_execucao)
        respostas_2 = prompt(self.perguntas_teste_unitario) if respostas_1['tipo_teste'] == 'Valor unitario' else prompt(self.perguntas_teste_range)

        ALGORITMO = respostas_1['algoritmo']
        TIPO_TESTE = respostas_1['tipo_teste']
        INICIO = respostas_2['inicio']
        FIM = respostas_2['fim'] if 'fim' in respostas_2 else respostas_2['inicio'] 

        return (ALGORITMO, INICIO, FIM)