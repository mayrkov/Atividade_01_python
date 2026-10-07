class Endereco:
    """Parte agregada ao Aluno: pode continuar existindo sem ele."""

    def __init__(self, rua: str, numero: str, bairro: str, cidade: str, cep: str):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep

    def validar_cep(self) -> bool:
        digitos = "".join(c for c in self.cep if c.isdigit())
        return len(digitos) == 8

    def formatar(self) -> str:
        return f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade} - CEP {self.cep}"

    def __str__(self) -> str:
        return self.formatar()
