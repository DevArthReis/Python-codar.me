def calculadora():
    conta = int(input("Se você deseja fazer conta de adição digite 1\nSe deseja fazer conta de subtração digite 2\nSe deseja fazer conta de divisão digite 3:\n"))
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    if conta == 1:
        resultado = numero1 + numero2
    elif conta == 2:
        resultado = numero1 - numero2
    elif conta == 3:
        resultado = numero1 / numero2
    else:
        return "Opção inválida"
    
    return resultado

resultado = calculadora()
print("O resultado da operação é:", resultado)
