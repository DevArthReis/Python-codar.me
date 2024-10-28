# main.py
from usuario import Usuario
from administrador import Administrador

# Criação de instâncias conforme especificado
u = Usuario("Gabriel", "gabriel@exemplo.com")
a = Administrador("Admin", "admin@exemplo.com")

# Chamando os métodos imprime_usuario
u.imprime_usuario()  # Saída esperada: Gabriel (gabriel@exemplo.com)
a.imprime_usuario()  # Saída esperada: Admin (admin@exemplo.com) – Administrador

# Exibindo a quantidade total de instâncias criadas
print(Usuario.quantidade)  # Saída esperada: 2
