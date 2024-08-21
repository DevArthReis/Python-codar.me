#Condicionais 
idade = int(input('Digite sua idade: '))

if idade >= 18 :
    print('adulto')
elif idade < 18 and idade >= 14 :
    print('Você e adolecente')
# se nem o as condiçoes if e nem as condiçoes elif servirem ele vai executar o else 
# Resumo do codigo: Se idade for maior ou igual a 18 print mario de idade, Se idade for menor que 18 e maior ou igual a 14 print adolecente 
# se nenhuma das condiçoes forem atendidas print menor de idade 
else:
    print('Kid')