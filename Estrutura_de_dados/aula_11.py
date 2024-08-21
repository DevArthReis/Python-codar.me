##tupla
pessoa = ("Gabriel",5002012,True)#<esta e a tupla.
#a parte de baixo e so um negocinho que eu quis fazer 
nome = pessoa[0]
senha = pessoa[1]
admin = pessoa[2]
chance = 0
while chance < 3:
   Senha = int(input('Digite sua Senha:'))
   if senha == Senha:
    print('Sua idade Esta no sistema ')   
    break
   elif Senha != senha:
     print('Senha incorreta,coloque uma senha valida')
     chance += 1
if chance == 3:
  print('Você não pode mais acessar')


# as tuplas são como se fosse uma lista
#  mais n podem ser modificadas 
# diferentemente da lista que utilizando metodos como o append 
# poderão ser feito mudanças.