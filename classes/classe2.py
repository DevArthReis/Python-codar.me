class Evento:
    def metodo_instancia(self):
        return ("metodo de instancia chamado",self)
    @classmethod
    def metodo_classe(cls):
        return("Metodo de classe chamado ",cls)
    @staticmethod#Por ser estatico este metodo é independente da classe evento
    def metodo_estatico():
        return"estatico chamado"
ev = Evento()
a = ev.metodo_instancia()# Evento.metodo_instancia()
print(a)#('metodo de instancia chamado', <__main__.Evento object ) ele ira printar a função metodo _instancia e o self vai ser subistituido para mostrar que ele é um objeto da classe Evento
b = Evento.metodo_classe()# Evento.metodo_clase(Evento)
print(b)# Evento.metodo_clase(Evento)
c = Evento.metodo_estatico()
print(c)