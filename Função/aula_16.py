def calcular_conta(consumo,taxa_servico,desconto_fidelidade): 
    servico = consumo * taxa_servico
    desconto =consumo * desconto_fidelidade
    valor = servico + consumo
    valor = valor - desconto
    return valor#return siginifica retorne o valor e tbm siginifica acabe a execução dessa função
    
valor =calcular_conta(consumo=100,taxa_servico=0.1,desconto_fidelidade=0.05)
print("o valor da conta ficou:",valor)
    