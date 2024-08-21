tentativa = ""
pais = "Brasil"
chance = 0 
while chance < 3:
    tentativa = str(input("Digite o Seu palpite:"))
    if tentativa == pais:
        print("Parabéns, você acertou!")
        break
    elif tentativa == "Chile":
        chance += 1
        print("o pais fica no mesmo continente que o seu palpite ")
        print("Vc errou,vc gastou",chance,"chance")
    elif tentativa != pais:
        chance += 1
        print("Vc errou,vc gastou",chance,"chance")
    
    
print("Vc perdeu seu burro, o pais era",pais)