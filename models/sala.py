class Sala:
    def __init__(
        self,
        escola,
        numero: int,
        capacidade: int,
        tipo: str = "aula",
    ):
        self.escola = escola
        self.numero = numero
        self.capacidade = capacidade
        self.tipo = tipo
        self.ocupada = False

    def ocupar(self) -> bool:
        """Marca a sala como ocupada. Retorna False se já estiver em uso."""
        if self.ocupada:
            return False
        self.ocupada = True
        return True

    def liberar(self) -> bool:
        """Libera a sala. Retorna False se já estiver livre."""
        if not self.ocupada:
            return False
        self.ocupada = False
        return True

    def __repr__(self) -> str:
        status = "ocupada" if self.ocupada else "livre"
        return f"Sala(numero={self.numero}, capacidade={self.capacidade}, {status})"
