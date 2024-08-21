alunos = [
("Alice", 8),
("Bob", 7),
("Carlos", 9)
]

soma = 0
quantidade = len(alunos)#len e usado para informar a quantidade de elementos(listas)


for item in alunos:
   soma = soma + item[1]
   media = soma / quantidade
   print("A media dos alunos e:",media)