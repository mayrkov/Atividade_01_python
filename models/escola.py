class Escola:
    def __init__(self, id: str, nome: str, cnpj: str, telefone: str):
        self.id = id
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self._salas = []
        self.ativa = True

    def criar_sala(self, numero: int, capacidade: int, **kwargs):
        """Cria uma Sala vinculada a esta Escola (composição)."""
        if not self.ativa:
            raise RuntimeError("Não é possível criar salas em uma escola fechada.")

        from .sala import Sala

        sala = Sala(self, numero, capacidade, **kwargs)
        self._salas.append(sala)
        return sala

    def listar_salas(self):
        return list(self._salas)

    def fechar(self):
        """Fecha a escola e destrói conceitualmente todas as salas (composição)."""
        for sala in self._salas:
            sala._desvincular()
        self._salas.clear()
        self.ativa = False
