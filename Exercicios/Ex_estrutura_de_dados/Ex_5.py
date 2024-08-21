alunos = [
{
"nome": "Alice",
"nota": 8,
},
{
"nome": "Bob",
"nota": 7,
},
{
"nome": "Carlos",
"nota": 9,
}
]
quantidade = len(alunos)
soma = 0 
for item in alunos:
    soma = soma + item["nota"]#ele indetifica que vc quer o value e soma os values de todas as notas nos dicts
    media = soma / quantidade#depois de somada ele divide as notas pela quantidade de dicts que vc tem dentro de alunos
    print(media)
