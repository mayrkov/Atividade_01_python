# Trabalho Prático 01

## Professor

### Atributos

| Atributo | Descrição |
|---|---|
| `id` | Identificador único do professor no sistema. |
| `nome` | Nome completo do professor. |
| `cpf` | CPF do professor. Ele existe como pessoa, sem depender de escola. |
| `disciplina` | Disciplina que o professor leciona. |
| `_escolas` | Lista das escolas em que o professor leciona (lado do professor na associação). |

### Métodos

| Método | Descrição |
|---|---|
| `vincular_escola(escola)` | Cria o vínculo entre o professor e uma escola, atualizando os dois lados. |
| `desvincular_escola(escola)` | Desfaz o vínculo. Professor e escola continuam existindo. |
| `listar_escolas()` | Retorna as escolas em que o professor leciona. |

## Relação Escola – Professor: Associação

A relação entre `Escola` e `Professor` é uma **Associação**, pelos motivos abaixo.

**1. Independência entre os objetos.** O professor não é criado dentro da escola nem pertence a ela. Os dois objetos são criados separadamente e só depois são ligados (`prof.vincular_escola(escola)`). Nenhum deles é "parte" do outro, então não existe relação todo-parte. Por isso a relação não é Agregação nem Composição.

**2. Muitos-para-muitos.** Um professor pode lecionar em várias escolas e uma escola pode ter vários professores. Como o professor não é exclusivo de uma escola, nenhuma das duas classes é dona da outra. A multiplicidade é `*` dos dois lados.

**3. Ciclos de vida separados.** A existência de um não depende da existência do outro:
- se a escola fechar, o professor continua existindo e pode continuar lecionando em outras escolas;
- se o professor sair, a escola continua funcionando com os demais professores.

Remover o vínculo só desfaz a ligação e não destrói nenhum dos objetos.

**Exemplo prático:** a professora Ana leciona Matemática na Escola Alfa e na Escola Beta. Se a Escola Alfa fechar, Ana continua existindo e lecionando na Escola Beta. O professor Carlos, que só dava aula na Alfa, também continua existindo e pode ser vinculado a outra escola. Esse caso está implementado no `main.py`.

### Modelagem

A associação é **bidirecional**:
- `Escola` guarda a lista `_professores`;
- `Professor` guarda a lista `_escolas`.

Ao vincular ou desvincular por qualquer um dos lados, a outra lista é atualizada automaticamente. Uma verificação (`if ... not in`) evita duplicar o vínculo.

No UML, a relação é representada por uma **linha simples** com multiplicidade `*` nas duas pontas:

```
Escola "*" ———————— "*" Professor
```
