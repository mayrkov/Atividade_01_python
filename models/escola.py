from models.sala import Sala


class Escola:
    def __init__(self, nome: str, cnpj: str, telefone: str):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.ativa = True
        # Composição: as salas são criadas e destruídas pela própria escola
        self._salas: list[Sala] = []
        # Associação: professores existem fora da escola
        self._professores = []

    # ---------- composição com Sala ----------
    def criar_sala(self, numero: str, capacidade: int, bloco: str) -> Sala:
        if not self.ativa:
            raise ValueError(f"A escola {self.nome} está fechada.")
        sala = Sala(numero, capacidade, bloco)
        self._salas.append(sala)
        return sala

    def listar_salas(self) -> list[Sala]:
        return list(self._salas)

    def fechar(self) -> None:
        # Ao fechar a escola, as salas deixam de existir no sistema
        self._salas.clear()
        for professor in list(self._professores):
            self.desvincular_professor(professor)
        self.ativa = False

    # ---------- associação com Professor ----------
    def vincular_professor(self, professor) -> None:
        if professor not in self._professores:
            self._professores.append(professor)
            professor.adicionar_escola(self)

    def desvincular_professor(self, professor) -> None:
        if professor in self._professores:
            self._professores.remove(professor)
            professor.remover_escola(self)

    def listar_professores(self) -> list:
        return list(self._professores)

    def __str__(self) -> str:
        status = "ativa" if self.ativa else "fechada"
        return (f"{self.nome} ({status}) - {len(self._salas)} sala(s), "
                f"{len(self._professores)} professor(es)")
