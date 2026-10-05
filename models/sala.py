class Sala:
    def __init__(
        self,
        escola,
        numero: int,
        capacidade: int,
        tipo: str = "aula",
    ):
        if escola is None:
            raise ValueError("Sala exige uma Escola: o vínculo é de composição.")

        self.escola = escola
        self.numero = numero
        self.capacidade = capacidade
        self.tipo = tipo
        self.ocupada = False

    def ocupar(self) -> bool:
        """Marca a sala como ocupada. Retorna False se já estiver em uso."""
        self._garantir_vinculo()
        if self.ocupada:
            return False
        self.ocupada = True
        return True

    def liberar(self) -> bool:
        """Libera a sala. Retorna False se já estiver livre."""
        self._garantir_vinculo()
        if not self.ocupada:
            return False
        self.ocupada = False
        return True

    def _desvincular(self) -> None:
        """Remove o vínculo com a Escola (chamado ao fechar a escola)."""
        self.escola = None
        self.ocupada = False

    def _garantir_vinculo(self) -> None:
        if self.escola is None:
            raise RuntimeError(
                "Esta sala não existe mais: a escola à qual pertencia foi fechada."
            )

    def __repr__(self) -> str:
        if self.escola is None:
            return f"Sala(numero={self.numero}, desvinculada)"
        status = "ocupada" if self.ocupada else "livre"
        return (
            f"Sala(numero={self.numero}, capacidade={self.capacidade}, "
            f"escola={self.escola.nome!r}, {status})"
        )
