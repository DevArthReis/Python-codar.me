notas = {
    "alice": 10,
    "bob": 8,
    "carol": 6,
}
for nota in notas:
    print(nota)
    print(notas[nota])

#para percorrer os dicts podemos usar o dict.items() o dict.values() e o dict.keys()
#tipo o exemplo a baixo

for nota in notas.items():
    print(nota)
    #printou "alice": 10,
    # "bob": 8,
    # "carol": 6,

for nota in notas.keys():
    print(nota)
    #printou alice
    # bob
    # carol


for nota in notas.values():
    print(nota)
    #printou 10
    # 8
    # 6

#O for e uma estrutura de repitição para vc usar quando vcc ja sabe quando vai acabar 
#O while e uma estrutura de repitição para vc usar quando vc nao sabe quando vai acabar
#Ex: para um sistema de login vc teria que usar um while [
#ja para percorrer os elementos presente em uma lista,tupla,set,dict o melhor seria usar um for 