#Conjuntos
usuarios = ["marcos","alice","joao","alice"] #isso e uma lista
usuarios_unicos = set(usuarios)
print("Esta e alista sem repetir os elementos por conta do set:",usuarios_unicos)
outros = ["marcos","patricio","joao","cristiano"]
print("A união das 2 listas e:",usuarios_unicos.union(outros))
print("Estes 2 estão presentes nas 2 listas:",usuarios_unicos.intersection(outros))
print("A diferença entre as 2 lista e :",usuarios_unicos.difference(outros))
# como os consjuntos n aceitam elementos repetidos 
# ao colocar a classe set em usuarios 
# ele elimina todos os elemtnos repetidos

#.union um metodo do conjunto para unir conjuntos
#.difference e um metodo para mostras as diferenças nas 2 listas
#.intersection mostra o que e igual nas 2 litas