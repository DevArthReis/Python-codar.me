def numero_primo():
    numero = int(input("Digite um número: "))
    if numero > 1:
        for i in range(2, numero):#range vai ser de 2 ate numero Ex: se numero for nove mais ficar assim o range 2,3,4,5,6,7,8
            if (numero % i) == 0:#% e o resto da divisão
                #no caso do exercicio se o resto da divisão do numero for igual a 0 ele n e primo
                return "Número não primo"
        return "Número primo"
    else:
        return "Número não primo"

# Chamada da função e impressão do resultado
resultado = numero_primo()
print(resultado)

"""range(x - (x-1))
range(2 x)
x = 9
range (2 - 9)
if (numero % 1) == 0
9 % 2
== 1
9 / 2 = 8 + 1
"""


    
        
    

    