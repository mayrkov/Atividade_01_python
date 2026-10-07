class Sala:
    """Só existe dentro de uma Escola (composição)."""

    def __init__(self, numero: str, capacidade: int, bloco: str):
        self.numero = numero
        self.capacidade = capacidade
        self.bloco = bloco
        self.ocupacao = 0

    def tem_vaga(self) -> bool:
        return self.ocupacao < self.capacidade

    def ocupar(self, quantidade: int) -> None:
        if self.ocupacao + quantidade > self.capacidade:
            raise ValueError(f"A sala {self.numero} comporta no máximo {self.capacidade} alunos.")
        self.ocupacao += quantidade

    def __str__(self) -> str:
        return f"Sala {self.numero} (bloco {self.bloco}) - {self.ocupacao}/{self.capacidade} lugares"
