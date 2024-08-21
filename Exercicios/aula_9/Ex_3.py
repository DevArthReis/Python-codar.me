nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')
if nome == 'arthur':
    print('Autenticado')
elif senha == '1234':
    print('Autenticado')
elif nome != 'arthur' or senha != '1234':
    print('Senha ou nome incorretos')    
