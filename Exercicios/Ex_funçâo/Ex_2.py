
def maior_numero(lista):
    
    if not lista:
        return None

   
    pos = 0
    num = lista[0]

   
    for i in range(1, len(lista)):
        if lista[i] > num:
            num = lista[i]
            pos = i

    return (pos, num)

# Exemplo de uso
lista_numeros = [10, 3, 15, 6, 8, 20, 7]
resultado = maior_numero(lista_numeros)
if resultado:
    print(f"A posição do maior número é {resultado[0]} e o maior número é {resultado[1]}.")
else:
    print("A lista está vazia.")



