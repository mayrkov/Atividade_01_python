# Trabalho Prático 01

**Cenário:** Sistema para gerenciar uma escola

**Integrantes:**

- _Nome 1_
- _Nome 2_
- _Nome 3_

---

## 1. Entidades: atributos e métodos

### Escola
| Atributos | Métodos |
|-----------|---------|
| `nome: str` | `criar_sala(numero, capacidade, bloco) -> Sala` |
| `cnpj: str` | `listar_salas() -> list[Sala]` |
| `telefone: str` | `vincular_professor(professor)` |
| `ativa: bool` | `desvincular_professor(professor)` |
| `_salas: list[Sala]` | `listar_professores() -> list` |
| `_professores: list[Professor]` | `fechar()` |

### Sala
| Atributos | Métodos |
|-----------|---------|
| `numero: str` | `tem_vaga() -> bool` |
| `capacidade: int` | `ocupar(quantidade)` |
| `bloco: str` | |
| `ocupacao: int` | |

### Professor
| Atributos | Métodos |
|-----------|---------|
| `nome: str` | `adicionar_escola(escola)` |
| `cpf: str` | `remover_escola(escola)` |
| `disciplina: str` | `listar_escolas() -> list` |
| `_escolas: list[Escola]` | `lecionar(turma) -> str` |

### Aluno
| Atributos | Métodos |
|-----------|---------|
| `nome: str` | `adicionar_nota(nota)` |
| `matricula: str` | `calcular_media() -> float` |
| `data_nascimento: str` | `atualizar_endereco(endereco)` |
| `notas: list[float]` | `remover() -> Endereco` |
| `endereco: Endereco` | |

### Endereco
| Atributos | Métodos |
|-----------|---------|
| `rua: str` | `validar_cep() -> bool` |
| `numero: str` | `formatar() -> str` |
| `bairro: str` | |
| `cidade: str` | |
| `cep: str` | |

---

## 2. Classificação das relações

| Relação | Tipo | Ciclo de vida | Exclusividade do "todo" | Existência independente |
|---------|------|---------------|--------------------------|-------------------------|
| Escola — Sala | **Composição** | Dependente | Sim | Não |
| Professor — Escola | **Associação** | Independente | Não | Sim |
| Aluno — Endereco | **Agregação** | Parcialmente dependente | Sim, enquanto o aluno existe | Sim |

### 2.1 Escola ◆— Sala: Composição
- **Ciclo de vida:** a sala é criada pela escola e, *"se a escola fechar, as salas deixam de existir"*. A parte morre junto com o todo.
- **Exclusividade:** cada sala pertence a uma única escola e não pode ser transferida.
- **Existência independente:** não existe. Uma sala sem escola *"não faz sentido"*.
- Por isso é uma relação todo–parte **forte**, ou seja, uma composição.

### 2.2 Professor —— Escola: Associação
- **Ciclo de vida:** *"a existência de um não depende da existência do outro"*. Se a escola fecha, o professor continua existindo, e o contrário também vale.
- **Exclusividade:** não há. A relação é **muitos-para-muitos**: um professor leciona em várias escolas e uma escola tem vários professores.
- **Existência independente:** sim, para os dois lados.
- Nenhum é "parte" do outro, eles só se relacionam. Por isso é uma **associação** simples.

### 2.3 Aluno ◇— Endereco: Agregação
- **Ciclo de vida:** o endereço é criado junto com o cadastro do aluno. Mas, se o aluno for removido, o endereço *"pode continuar a fazer sentido isoladamente"* (por exemplo, em relatórios) e é *"repassado a outro contexto"*.
- **Exclusividade:** enquanto o aluno existe, o endereço é dele.
- **Existência independente:** sim. A parte sobrevive à destruição do todo.
- É uma relação todo–parte (o aluno **tem** um endereço), mas **fraca**, porque a parte não morre junto com o todo. Por isso é uma **agregação**.

> **Por que não é composição?** O endereço nasce junto com o aluno, o que lembra uma composição. Mas o critério que decide é o que acontece **na destruição**. Na composição, a parte é destruída junto com o todo. Aqui o endereço continua existindo, então a relação é agregação.

---

## 3. Diagrama de classes UML

O arquivo editável está em `assets/diagrama_uml.drawio` e abre em [app.diagrams.net](https://app.diagrams.net).

| Relação | Notação usada |
|---------|---------------|
| Escola ◆—— Sala | Losango **preenchido** do lado da Escola (composição), multiplicidade 1 → 1..* |
| Professor —— Escola | Linha **simples** (associação), multiplicidade 0..* ↔ 0..* |
| Aluno ◇—— Endereco | Losango **vazado** do lado do Aluno (agregação), multiplicidade 1 → 1 |

Representação textual:

```
┌──────────────┐ 0..*      0..* ┌──────────────┐ 1 ◆────── 1..* ┌──────────┐
│  Professor   │────────────────│    Escola    │────────────────│   Sala   │
└──────────────┘                └──────────────┘                └──────────┘

┌──────────────┐ 1 ◇────── 1 ┌──────────────┐
│    Aluno     │─────────────│   Endereco   │
└──────────────┘             └──────────────┘
```

---

## 4. Implementação em Python

O código está na pasta `models/` e a demonstração em `main.py`.

### Composição: a escola cria e destrói as salas

```python
class Escola:
    def criar_sala(self, numero, capacidade, bloco) -> Sala:
        sala = Sala(numero, capacidade, bloco)   # a sala só nasce pela escola
        self._salas.append(sala)
        return sala

    def fechar(self) -> None:
        self._salas.clear()                      # salas deixam de existir
        ...
```

### Associação: vínculo N:N nos dois sentidos

```python
class Escola:
    def vincular_professor(self, professor) -> None:
        if professor not in self._professores:
            self._professores.append(professor)
            professor.adicionar_escola(self)     # recebe um professor que já existe
```

### Agregação: o endereço é criado com o aluno, mas sobrevive a ele

```python
class Aluno:
    def __init__(self, nome, matricula, data_nascimento, rua, numero, bairro, cidade, cep):
        ...
        self.endereco = Endereco(rua, numero, bairro, cidade, cep)

    def remover(self) -> Endereco:
        endereco = self.endereco
        self.endereco = None
        return endereco                          # repassado a outro contexto
```

### Executar

```bash
python main.py
```
