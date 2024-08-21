def conta():
    consumo = int(input("Digite o valor do consumo: "))
    taxa_servico = float(input("Digite a taxa de serviço: "))
    desconto = float(input("Digite o desconto: "))

    valor_da_taxa = consumo * taxa_servico
    valor_com_taxa = consumo + valor_da_taxa

    if consumo >= 100:
        valor_do_desconto = valor_com_taxa * desconto
        valor_final = valor_com_taxa - valor_do_desconto
    else:
        valor_final = valor_com_taxa

    return valor_final

valor_final = conta()
print(f"O valor final é: {valor_final}")



"""conta_taxa = consumo * taxa_servico
    valor = conta_taxa + consumo
    conta_desconto = consumo * desconto
    valor_final = valor - conta_desconto  """

#so pra registrar fiz esse codigo totalmente da minha cabeça 
#to feliz de mais :)
    
    
    