class Professor:
    """Associação N:N com Escola - nenhum dos dois depende do outro para existir."""

    def __init__(self, nome: str, cpf: str, disciplina: str):
        self.nome = nome
        self.cpf = cpf
        self.disciplina = disciplina
        self._escolas = []

    def adicionar_escola(self, escola) -> None:
        if escola not in self._escolas:
            self._escolas.append(escola)
            escola.vincular_professor(self)

    def remover_escola(self, escola) -> None:
        if escola in self._escolas:
            self._escolas.remove(escola)
            escola.desvincular_professor(self)

    def listar_escolas(self) -> list:
        return list(self._escolas)

    def lecionar(self, turma: str) -> str:
        return f"{self.nome} está lecionando {self.disciplina} para a turma {turma}."

    def __str__(self) -> str:
        escolas = ", ".join(e.nome for e in self._escolas) or "nenhuma escola"
        return f"Prof. {self.nome} ({self.disciplina}) - leciona em: {escolas}"
