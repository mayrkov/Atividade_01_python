from models.escola import Escola
from models.professor import Professor
from models.aluno import Aluno


def titulo(texto: str) -> None:
    print(f"\n{'=' * 10} {texto} {'=' * 10}")


def main() -> None:
    # ---------- Composição: Escola ◆ Sala ----------
    titulo("Composição: Escola -> Sala")
    escola_a = Escola("Escola Estadual Machado de Assis", "11.111.111/0001-11", "(11) 4000-0001")
    escola_b = Escola("Colégio Monteiro Lobato", "22.222.222/0001-22", "(11) 4000-0002")

    sala1 = escola_a.criar_sala("101", 35, "A")
    escola_a.criar_sala("102", 30, "A")
    escola_b.criar_sala("201", 40, "B")
    sala1.ocupar(28)

    for sala in escola_a.listar_salas():
        print(sala)

    # ---------- Associação: Professor — Escola ----------
    titulo("Associação: Professor <-> Escola (N:N)")
    ana = Professor("Ana Souza", "123.456.789-00", "Matemática")
    carlos = Professor("Carlos Lima", "987.654.321-00", "História")

    escola_a.vincular_professor(ana)
    escola_b.vincular_professor(ana)     # um professor em várias escolas
    escola_a.vincular_professor(carlos)  # uma escola com vários professores

    print(ana)
    print(carlos)
    print(ana.lecionar("9º ano A"))

    # ---------- Agregação: Aluno ◇ Endereco ----------
    titulo("Agregação: Aluno -> Endereco")
    aluno = Aluno("Pedro Alves", "2026001", "15/03/2010",
                  "Rua das Flores", "123", "Centro", "São Paulo", "01001-000")
    aluno.adicionar_nota(8.5)
    aluno.adicionar_nota(7.0)
    print(aluno)
    print(f"Endereço criado junto com o aluno: {aluno.endereco} | CEP válido: {aluno.endereco.validar_cep()}")

    endereco_para_relatorio = aluno.remover()
    del aluno
    print(f"Aluno removido. Endereço continua existindo para relatório: {endereco_para_relatorio}")

    # ---------- Ciclo de vida: fechar a escola ----------
    titulo("Fechando a escola")
    print(f"Antes:  {escola_a}")
    escola_a.fechar()
    print(f"Depois: {escola_a}")
    print(f"Salas de {escola_a.nome}: {escola_a.listar_salas()}  <- deixaram de existir (composição)")
    print(f"{ana}  <- professora continua existindo (associação)")
    print(f"{carlos}  <- professor continua existindo, mesmo sem escola")


if __name__ == "__main__":
    main()
