np = ""
numero = 8
chance = 0
while chance < 3:
     np = int(input("digite um numero: "))
     if np == numero:
        print('Vc ganhou')
        break
     elif numero >= 11:
      print("Seu número está entre 1 e 10!")
      chance += 1
     elif np < numero:
      print("mais alto")
      chance += 1    
     elif np > numero:
      print("mais baixo")
      chance += 1
    

if chance == 3:
     print("vc perdeu")

    
    
  
