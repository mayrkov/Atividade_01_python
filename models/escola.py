class Escola:
    def __init__(self, id: str, nome: str, cnpj: str, telefone: str):
        self.id = id
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self._salas = []

    def criar_sala(self, numero: int, capacidade: int, **kwargs):
        from .sala import Sala
        sala = Sala(self, numero, capacidade, **kwargs)
        self._salas.append(sala)
        return

    def listar_salas(self):
        return list(self._salas)
