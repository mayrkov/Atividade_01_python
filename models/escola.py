class Escola:
    def __init__(self, id: str, nome: str, cnpj: str, telefone: str):
        self.id = id
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self._salas = []
        self._professores = []

    def criar_sala(self, numero: int, capacidade: int, **kwargs):
        from .sala import Sala
        sala = Sala(self, numero, capacidade, **kwargs)
        self._salas.append(sala)
        return

    def listar_salas(self):
        return list(self._salas)

    def adicionar_professor(self, professor):
        # Associação: o professor é criado fora da escola e apenas vinculado a ela
        if professor not in self._professores:
            self._professores.append(professor)
            professor.vincular_escola(self)

    def remover_professor(self, professor):
        if professor in self._professores:
            self._professores.remove(professor)
            professor.desvincular_escola(self)

    def listar_professores(self):
        return list(self._professores)
