aluno = ["Arthur",20,"Brasileiro"]
print('O aluno',aluno[0],'tem',aluno[1],'anos e tem nacionalidade', aluno[2],)

alunos = [
    ['Arthur',20,'Brasileiro'],#0
    ['João', 21, 'Brasileiro'],#1
    ['Maria', 19, 'Brasileira']#2


]
print(alunos[0])
print(alunos[2])

notas = [8,9,10,7,3]
i = 0
total = 0
qtd = len(notas)
print('Aquantidade de itens na lista e',qtd)
while i < qtd:
    total = total + notas[i]
    i = i + 1

print('O total das notas da:',total)
media = total / 5
print('A média das notas é:',media)