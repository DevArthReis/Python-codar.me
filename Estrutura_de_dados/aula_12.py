#conjuntos
usuarios = {"Arthur","Joao"}#Este e um Conjunto
#poderia ser assim tbm
#usuarios = set(["Arthur","Joao"])#Este e um Conjunto
#Abaixo e um teste que eu crie pra fixar
print("Os usuarios do sistema são:",usuarios)
novo_usuario = str(input("Adicione o novo usuario: "))
usuarios.add(novo_usuario)
usuarios_sem_repetir = set(usuarios)
print(novo_usuario,"Foi adicionado a lista:",usuarios)

#Conjuntos não permitam elementos repetidos
#O set n deixa os elementos se repetirem
# Para uma lista ou uma tupla virarem um conjunto e 
# so colocarem entre um set()
#set e = a conjunto
#.add e um methodo do set para adicionar algo ao conjunto
