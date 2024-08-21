valor_de_compra = float(input('Digite o valora da compra: '))
valor_do_frete = float(input('Digite o valor do frente: '))
client_cadastrado = str(input('Vc e cadastrado ? Digite s ou n: '))

Soma = valor_de_compra + valor_do_frete >= 100

cadastrado_1 = client_cadastrado == 's'


resultado =  Soma or cadastrado_1
print('Pode receber o cumpom:',resultado)
