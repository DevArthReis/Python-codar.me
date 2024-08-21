
num = int(input('Digite um número: '))
vezes_que_ele_pode_ser_divisivel = 0#Esta variavel vai contar ali embaixo quantas vezes o numero que vc escolheu foi dividido
for c in range(1, num+1):#Para cada item no range entre 1 e o numero que vc escolheu +1 pois o python exclui 1 item ele vai citar o range
    if num % c == 0:# se o resto da divisão entre o numero que vc escolheu e os itens do range for 0.
        vezes_que_ele_pode_ser_divisivel += 1#Ele vai adicionar mais 1  a variavel vezes_que_ele_pode_ser_divisivel
if vezes_que_ele_pode_ser_divisivel == 2:#logo se a variavel vezes chegar a 2 o numero e primo 
    print('O número é primo.')
else:#Se não chegar ou ultrapassar ele este numero n sera primo.
    print('O número não é primo.')







