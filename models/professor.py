class Professor:
    def __init__(self, id: str, nome: str, cpf: str, disciplina: str):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.disciplina = disciplina
        self._escolas = []

    def vincular_escola(self, escola):
        # Associação bidirecional: o professor guarda a escola e a escola guarda o professor
        if escola not in self._escolas:
            self._escolas.append(escola)
            escola.adicionar_professor(self)

    def desvincular_escola(self, escola):
        # Remove apenas o vínculo; professor e escola continuam existindo
        if escola in self._escolas:
            self._escolas.remove(escola)
            escola.remover_professor(self)

    def listar_escolas(self):
        return list(self._escolas)
