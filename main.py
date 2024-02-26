from professor import Professor
from aluno import Aluno
from aula import Aula

professor1 = Professor("Lucca")
professor1.ministrar_aula("Matemática")

aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")

aula = Aula(professor1, "Programação Orientada a Objetos")

aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)

print(aula.listar_presenca())