class Resultado():
    def __init__(self, tempo_inicial, tempo_final, algoritimo, n, resultado):
        self.tempo_inicial = tempo_inicial
        self.tempo_final = tempo_final
        self.algoritimo = algoritimo
        self.n = n
        self.resultado = resultado
        self.tempo_execucao = (self.tempo_final - self.tempo_inicial) / (10 ** 9)

    def get_tempo(self):
        return "{:f}".format(self.tempo_execucao)

    def __str__(self):
        string_of_object = '{}({}) = {} :: => {} segundos'.format(self.algoritimo, self.n, self.resultado, str(self.get_tempo()))
        return string_of_object