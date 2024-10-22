class Evento:
    id = 1
    # a função init serve pra inicializar a classe e passar as instancias que serão usadas como é base no codigo
    def __init__(self, nome, local=""):  # Inicializa a classe com um nome e um local (opcional)
        self.nome = nome  # instancia inicializada da classe
        self.local = local  # instancia inicializada da classe
        self.id = Evento.id
        Evento.id += 3

    def imprime_informações(self):
        # Método que imprime as informações do evento
        print("Id do evento", self.id)# Imprime id do evento
        print("Nome do evento:", self.nome)  # Imprime o nome do evento
        print("Local do evento:", self.local)  # Imprime o local do evento
        print("----------------")

    @classmethod
    def cria_evento_online(cls, nome):
        # Método de classe que cria um evento online com um link fixo
        evento = cls(nome, local=f"https://tamarcado.com/eventos?id{cls.id}")  # Cria um evento online
        return evento  # Retorna o evento criado

    @staticmethod
    def calcula_limite_pessoas_area(area):
        # Método estático que calcula o limite de pessoas com base na área fornecida
        if 5 <= area < 10:
            return 5  # Limite de 5 pessoas para área entre 5 e 10
        elif 10 <= area < 20:
            return 15  # Limite de 15 pessoas para área entre 10 e 20
        else:
            return 0  # Limite de 0 pessoas para áreas menores que 5 ou maiores ou iguais a 20

# Exemplos de uso da classe Evento
ev_online = Evento.cria_evento_online("Aula de Python")  # Cria um evento sem especificar o local
ev2_online = Evento.cria_evento_online("Aula de js")  # Cria um evento com local específico
ev_online.imprime_informações()  # Imprime as informações do segundo evento (nome e local)
ev2_online.imprime_informações()