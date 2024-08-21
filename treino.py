np =  ""
numero = 5 
chance = 0
print('Vc tem 3 chances para descobrir o numero secreto')
while chance < 3:
    np = int(input('Digite um numero:'))
    if np == numero:
        print('Vc ganhou!!')
        break
    elif np == 10:
        print('O numero secreto esta entre 10 e 1 ')
        chance += 1
    elif np > numero:
        print('Vc errou, o numero é menor')
        chance += 1
    elif np < numero:
        print('Vc errou, o numero é maior ')
        chance += 1
if chance == 4:
    print('Vc perder loser')   
 #exercicio de insonia :)

