class Evento:
    def metodo_instancia(self):
        return ("Método de instância chamado", self)

    @classmethod
    def metodo_classe(cls):
        return ("Método de classe chamado", cls)

    @staticmethod  # Por ser estático, este método é independente da classe Evento
    def metodo_estatico():
        return "Estático chamado"

ev = Evento()
a = ev.metodo_instancia()  # Chama o método de instância
print(a)  # ('Método de instância chamado', <__main__.Evento object>) ele irá imprimir a função metodo_instancia e o self será substituído para mostrar que ele é um objeto da classe Evento

b = Evento.metodo_classe()  # Chama o método de classe
print(b)  # ('Método de classe chamado', <class '__main__.Evento'>)

c = Evento.metodo_estatico()  # Como ele é independente, ele apenas imprime o valor da função metodo_estatico sem mais nada
print(c)
