#loop
total = 0
continuar = "s"
while continuar == "s":
    valor= float(input('Digite o valor da compra: '))
    total = total + valor 
    continuar = input('Deseja continuar? (s/n)')

print('Valor total seria de', total)
#while e igual a enquanto
#resumo do codigo: total e igual a 0 continuar e igual a s enquanto continuar for igual a s o 
# console ira pedir o valor da compra e somara com o total, caso continuar receba um valor diferente de s
# o loop sera encerrado e o valor total sera impresso no console