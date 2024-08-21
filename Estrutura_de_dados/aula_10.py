#lista(list)
notas = [8,10,7.5]
#        0  1  2 ...
print(notas[0])
print(notas[2])
peso = [3,7,8]# 9
#       0 1 2  3 ...
peso.append(9)#^   o methodo append deixa vc adicionar algo a lista que vc criou  
print(peso[3])
notas.sort()#methodo sort deixa sua lista seguindo uma ordem crecente 
peso.sort()
print(notas)
print(peso)
x = notas.pop() #o pop pega um numero  da lista 
y = peso.pop()
print(x)
print(y)
print(peso)
print(notas)
notas.insert(10,8)# insert ele inseri um valor a sua lista 
print("apos a inserção as notas ficam")
print(notas)
peso.insert(8,10)
print("apos a inserção os pesos ficam")
print(peso)
notas.pop(0)#ele vai retirar o 7.5 pois ele esta no espaço 0 presente no parenteses
print("apos a remoção as notas ficam")
print(notas)
# em listas se usa indices como por exemplo
#nota = [1,2,3]o 3 vai se encotrar no indice 2 
#        0 1 2

