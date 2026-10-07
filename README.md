# TP01 – Arquitetura de Software

Sistema para gerenciar uma escola, modelado com orientação a objetos em Python, com foco nos relacionamentos **associação**, **agregação** e **composição**.

## Estrutura

```
tp01-arquitetura-software/
├── models/
│   ├── escola.py      # Escola – compõe Sala, associa-se a Professor
│   ├── sala.py        # Sala
│   ├── professor.py   # Professor
│   ├── aluno.py       # Aluno – agrega Endereco
│   └── endereco.py    # Endereco
├── assets/
│   └── diagrama_uml.drawio   # Diagrama de classes (abrir em app.diagrams.net)
├── main.py                   # Demonstração
├── Trabalho Prático 01 doc.md    # Respostas das questões
├── README.md
└── .gitignore
```

## Como executar

Requer Python 3.9 ou superior. Não usa bibliotecas externas.

```bash
python main.py
```

## Relacionamentos

| Relação | Tipo |
|---------|------|
| Escola ◆ Sala | Composição |
| Professor — Escola | Associação (N:N) |
| Aluno ◇ Endereco | Agregação |
