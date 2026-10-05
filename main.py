from models.escola import Escola
from models.professor import Professor


# --- Associação: Escola - Professor ---
escola_a = Escola("1", "Escola Alfa", "11.111.111/0001-11", "(11) 1111-1111")
escola_b = Escola("2", "Escola Beta", "22.222.222/0001-22", "(22) 2222-2222")

# Professores são criados independentemente de qualquer escola
prof_ana = Professor("1", "Ana", "111.111.111-11", "Matemática")
prof_carlos = Professor("2", "Carlos", "222.222.222-22", "História")

# Muitos-para-muitos: Ana leciona em duas escolas e a Escola Alfa tem dois professores
prof_ana.vincular_escola(escola_a)
prof_ana.vincular_escola(escola_b)
escola_a.adicionar_professor(prof_carlos)

print("Professores da Escola Alfa:", [p.nome for p in escola_a.listar_professores()])
print("Escolas da Ana:", [e.nome for e in prof_ana.listar_escolas()])

# A Escola Alfa "fecha": desfazemos os vínculos, mas os professores continuam existindo
for professor in escola_a.listar_professores():
    escola_a.remover_professor(professor)
del escola_a

print("Escolas da Ana após o fechamento da Alfa:", [e.nome for e in prof_ana.listar_escolas()])
print("Carlos continua existindo:", prof_carlos.nome, "-", prof_carlos.disciplina)
