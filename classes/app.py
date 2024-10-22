from evento2 import Evento
from evento_online import EventoOnline
ev_online = EventoOnline("Aula de Python")  # Cria um evento online sem especificar o local
ev2_online = EventoOnline("Aula de JS")  # Cria outro evento online

# Imprime as informações do evento online criado
ev_online.imprime_informações()  # Imprime as informações do primeiro evento online
ev2_online.imprime_informações()  # Imprime as informações do segundo evento online
ev = Evento("Aula de python","Rio de janeiro")
ev.imprime_informações()



