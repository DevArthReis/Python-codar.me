class Evento():
    def AlteraNomeEvento(self,novo_nome):#este self que esta sendo passado nos argumentos é um padrao do python 
        print("Alterando o nome do evento")#dps ele vai executar este print dentro da função
        self.nome = novo_nome

ev= Evento()
ev.nome = "aula de python"
print(ev.nome)#Primeiro ele vai executar este pequeno bloco de codigo 


ev.AlteraNomeEvento("aula de javascript")#dps de executar o print da função ele a função vai ser chama aqui e vai mudar o nome da variavel ev.nome
print(ev.nome)#por ultimo ele vai printar o novo ev.nome que foi passado na argumento acima 
