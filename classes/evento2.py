class Evento:
    id = 1  # Atributo de classe para controlar a contagem de IDs dos eventos

    # O método __init__ é o construtor da classe, utilizado para inicializar as instâncias
    def __init__(self, nome, local=""):  # Recebe o nome do evento e um local (opcional)
        self.nome = nome  # Atribui o nome do evento à instância
        self.local = local  # Atribui o local do evento à instância
        self.id = Evento.id  # Atribui um ID único à instância, retirado do atributo de classe
        Evento.id += 1  # Incrementa o ID de classe para o próximo evento criado

    def imprime_informações(self):
        # Método que imprime as informações do evento
        print(f"Id do evento: {self.id}")  # Imprime o ID do evento
        print(f"Nome do evento: {self.nome}")  # Imprime o nome do evento
        print(f"Local do evento: {self.local}")  # Imprime o local do evento
        print("----------------")  # Imprime uma linha separadora para melhor visualização

    

    @staticmethod
    def calcula_limite_pessoas_area(area):
        # Método estático que calcula o limite de pessoas baseado na área fornecida
        if 5 <= area < 10:
            return 5  # Limite de 5 pessoas para área entre 5 e 10
        elif 10 <= area < 20:
            return 15  # Limite de 15 pessoas para área entre 10 e 20
        else:
            return 0  # Limite de 0 pessoas para áreas menores que 5 ou maiores ou iguais a 20
class EventoOnline(Evento):#EventoOnline é a expecialização da classe Evento/EventoOnline tem tudo que tem na Classe Evento porem ela vai ter algumas modificações que Evento n tem.
    def __init__(self, nome, _=""):  # Recebe o nome do evento e um local (opcional)
        local = f"https://tamarcado.com/eventos?id{EventoOnline.id}"
        Evento.__init__(self,nome,local)
        
    def imprime_informações(self):
        # Método que imprime as informações do evento
        print(f"Id do evento: {self.id}")  # Imprime o ID do evento
        print(f"Nome do evento: {self.nome}")  # Imprime o nome do evento
        print(f"Linke para acessar evento: {self.local}")  # Imprime o local do evento
        print("----------------")
    
        

# Exemplos de uso da classe Evento
ev_online = EventoOnline("Aula de Python")  # Cria um evento online sem especificar o local
ev2_online = EventoOnline("Aula de JS")  # Cria outro evento online

# Imprime as informações do evento online criado
ev_online.imprime_informações()  # Imprime as informações do primeiro evento online
ev2_online.imprime_informações()  # Imprime as informações do segundo evento online
ev = Evento("Aula de python","Rio de janeiro")
ev.imprime_informações()

#Esta aula foi de herança entre classes.