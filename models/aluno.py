class Aluno:
    def __init__(self, nome, matricula, endereco):
        self.nome = nome
        self.matricula = matricula
        self.endereco = endereco

    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Endereço: {self.endereco.formatar()}")

    def atualizar_endereco(self, novo_endereco):
        self.endereco = novo_endereco