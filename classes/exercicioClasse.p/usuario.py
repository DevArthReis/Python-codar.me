# usuario.py

class Usuario:
    quantidade = 0  # Atributo de classe para contar o número de instâncias

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        Usuario.quantidade += 1  # Incrementa o contador cada vez que uma instância é criada

    def imprime_usuario(self):
        print(f"{self.nome} ({self.email})")

# Exemplo de classe que herda de Usuario
class Administrador(Usuario):
    def __init__(self, nome, email, nivel_acesso):
        super().__init__(nome, email)
        self.nivel_acesso = nivel_acesso

# Teste da implementação
if __name__ == "__main__":
    user1 = Usuario("Gabriel", "gabriel@exemplo.com")
    user1.imprime_usuario()
    print("Quantidade de instâncias:", Usuario.quantidade)

    admin1 = Administrador("Alice", "alice@exemplo.com", "super")
    admin1.imprime_usuario()
    print("Quantidade de instâncias:", Usuario.quantidade)

          
    
    