a= int(input('Digite um numero: '))
b= int(input('Digite um numero: '))
c= int(input('Digite: \n 1 para somar  \n 2 para subtrair \n 3 para multiplicar \n 4 para dividir\n:   '))


if c == 4 and b == 0 or a == 0:
    print('Não é possivel dividir por zero')
elif c==1:
    print(a+b)    
elif c ==2:
    print(a-b)
elif c ==3:
    print(a*b)
elif c == 4:
    print(a/b)
          



