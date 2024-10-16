class Evento:
    def __init__(self,nome,local=""):#Passando um atributo
        self.nome = nome
        self.local = local
    def imprime_informações(self):
        print("Nome do evento:",self.nome)
        print("Local do evento:",self.local)
    
ev = Evento("Aula de Python")
ev2 = Evento("Aula de python","Distrito Federal")#dando valor aos atributos
print(ev.local)
ev2.imprime_informações()#Imprime o valor que foi passado no ev2 para oself.nome e o self.local