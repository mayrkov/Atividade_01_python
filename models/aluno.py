from models.endereco import Endereco


class Aluno:
    def __init__(self, nome: str, matricula: str, data_nascimento: str,
                 rua: str, numero: str, bairro: str, cidade: str, cep: str):
        self.nome = nome
        self.matricula = matricula
        self.data_nascimento = data_nascimento
        self.notas: list[float] = []
        # Agregação: o endereço nasce junto com o cadastro do aluno...
        self.endereco = Endereco(rua, numero, bairro, cidade, cep)

    def adicionar_nota(self, nota: float) -> None:
        if not 0 <= nota <= 10:
            raise ValueError("A nota deve estar entre 0 e 10.")
        self.notas.append(nota)

    def calcular_media(self) -> float:
        return sum(self.notas) / len(self.notas) if self.notas else 0.0

    def atualizar_endereco(self, endereco: Endereco) -> None:
        self.endereco = endereco

    def remover(self) -> Endereco:
        # ...mas, quando o aluno é removido, o endereço é repassado a outro contexto
        endereco = self.endereco
        self.endereco = None
        return endereco

    def __str__(self) -> str:
        return f"{self.nome} (matrícula {self.matricula}) - média {self.calcular_media():.1f}"
