from models import Escola


def main():
    escola = Escola(
        id="1",
        nome="Escola Municipal Centro",
        cnpj="12.345.678/0001-90",
        telefone="(11) 4002-8922",
    )

    sala_101 = escola.criar_sala(101, 40, tipo="aula")
    sala_lab = escola.criar_sala(202, 25, tipo="laboratorio")

    print("=== Após criar salas ===")
    print("Salas da escola:", escola.listar_salas())
    print("Sala 101 vinculada a:", sala_101.escola.nome)

    sala_101.ocupar()
    print("Sala 101 ocupada?", sala_101.ocupada)

    # Composição: ao fechar a escola, as salas deixam de existir conceitualmente
    escola.fechar()

    print("\n=== Após fechar a escola ===")
    print("Escola ativa?", escola.ativa)
    print("Salas restantes na escola:", escola.listar_salas())
    print("Sala 101:", sala_101)
    print("Sala lab:", sala_lab)
    print("Vínculo sala_101.escola:", sala_101.escola)


if __name__ == "__main__":
    main()
