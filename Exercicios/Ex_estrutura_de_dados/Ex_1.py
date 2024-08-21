lista = []
n = " "
while n:
    n = int(input("adicione um número a lista: "))# no input vc digita o numero que deseja adicionar
    lista.append(n)#O append vcc usa para colar os elemtnos que vc vai digitando dentro da lista
    if n > 0:
        continue
    else:
        
        break

print(lista)



