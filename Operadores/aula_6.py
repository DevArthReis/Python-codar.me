#Operadores logicos
# not 
# and
# or

# not

idade = 16 
maior_de_idade = idade >= 18
menor_de_idade = not maior_de_idade
print ('A idade dele e :',idade)
print('e maior de idade ?',maior_de_idade)
print('e menor de idade ? ',menor_de_idade)
# O operador logico not inverte o valor das variaveis se um for verdadeito o outro sera falso
# ( no caso acima se idade for maior ou igual a 18 ele vai falar que e true maior de idade,
#  se for menor que 18 vai falar que menor de idade e true  )

# and
senha = True
usuario = True
sucesso = senha and usuario
print ('O login foi feito com sucesso:', sucesso)
# O operador logico and e basicamente um e 
# ( dentro do exemplo acima ele diz que senha e usuario são sucesso
#  pois os 2 são verdadeiros o and so esta fazendo a junçao dos 2 )

# or
idade = 18
idade_minima = 16
acompanhada_pelos_pais = False
pode_assistir = idade >= idade_minima or acompanhada_pelos_pais
print ('Pode assistir ao filme?', pode_assistir)
 # O operador logico de or e basicamente um ou 
 # ( dentro do exemplo acima ele diz que se idade for superior ou igual a idade minimo  
 # ou estiver acompanhada for true logo pode assistir)

