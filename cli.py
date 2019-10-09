PRETO = "\033[1;30m"
VERMELHO = "\033[1;31m"
VERDE = "	\033[1;32m"
AMARELO = "\033[1;33m"
AZUL = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
CINZA_CLARO = "\033[1;37m"
CINZA_ESCURO = "\033[1;90m"
VERMELHO_CLARO = "\033[1;91m"
VERDE_CLARO = "\033[1;92m"
AMARELO_CLARO = "\033[1;93m"
AZUL_CLARO = "\033[1;94m"
MAGENTA_CLARO = "\033[1;95m"
CYAN_CLARO = "\033[1;96m"
BRANCO = "\033[1;97m"
NEGRITO = "\033[;1m"
INVERTE = "\033[;7m"
RESET = "\033[0;0m"

testes = []
algoritmo = []

perguntas = {
    #"testes" : "Qual tipo de execução deseja testar?",
    "algoritmo" : "Qual algoritmo deseja testar?",
    "valor" : "Qual numero deseja?"
}

opcoes = {
    #"testes" : testes,
    "algoritmo" : algoritmo
}

cores_prints = {
    "pergunta" : BRANCO,
    "resposta" : AZUL_CLARO,
    "opcao" : VERMELHO
}

def setar_opcoes(testes, algoritmo):
    #opcoes["testes"] = testes
    opcoes["algoritmo"] = algoritmo
    

def get_respostas():
    respostas = {}
    for pergunta in perguntas.keys():
        print("?", cores_prints["pergunta"], perguntas[pergunta])

        if pergunta in opcoes and len(opcoes[pergunta]) > 0:
            ops_pergunta = opcoes[pergunta]
            for opcao in ops_pergunta:
                str_opcao = "{}{}{} - {}".format(cores_prints["opcao"], ops_pergunta.index(opcao), RESET, str(opcao))
                print(str_opcao)
        
        resposta_valida = False
        while (not resposta_valida):
            resposta = input(cores_prints["resposta"] + "> ")
            resposta_valida = valida_resposta(pergunta, resposta)

        resposta = int(resposta)
        respostas[pergunta] = opcoes[pergunta][resposta] if pergunta in opcoes else resposta
        print(RESET)

    return respostas

def valida_resposta(pergunta, resposta):
    if resposta.isnumeric():
        if pergunta in opcoes:
            if int(resposta) < len(opcoes[pergunta]):
                return True
        else:
            return True
    print(VERMELHO,"Opção invalida.",RESET)
    return False