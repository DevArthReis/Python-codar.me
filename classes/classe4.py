# Classe base
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def descricao(self):
        return f"Veículo: {self.marca} {self.modelo}"
    
    def mover(self):
        return "O veículo está se movendo."

# Classe derivada
class Carro(Veiculo):
    def __init__(self, marca, modelo, tipo_combustivel):
        # Chamando o construtor da classe base
        super().__init__(marca, modelo)
        self.tipo_combustivel = tipo_combustivel

    def descricao(self):
        # Sobrescrevendo o método da classe base
        return f"Carro: {self.marca} {self.modelo}, Combustível: {self.tipo_combustivel}"
    
    def buzinar(self):
        return "Bip Bip!"

# Exemplo de uso
meu_carro = Carro("Toyota", "Corolla", "Gasolina")
print(meu_carro.descricao())  # Saída: Carro: Toyota Corolla, Combustível: Gasolina
print(meu_carro.mover())      # Saída: O veículo está se movendo.
print(meu_carro.buzinar())    # Saída: Bip Bip!
