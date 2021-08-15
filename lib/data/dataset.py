class Dados:
    def __init__(self):
        self._dados = []

    def __str__(self):
        return f'{self._dados}'

    @property
    def dados(self):
        return self._dados

    def add_dado(self, dado):
        self._dados.append(dado)