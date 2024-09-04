class pc:
    def __init__(self,marca,memoria,processador):
        self.marca = marca
        self.memoria = memoria
        self.processador = processador
    
    def Ligar(self):
        print("estou ligando")

    def Desligar(self):
        print("estou desligando")

    def ExibirinformaçoesDestePc(self):
        print(self.marca,self.memoria,self.memoria)

pc1 = pc('asus','16gb','A520m')
pc1.Ligar()
pc1.Desligar()
pc1.ExibirinformaçoesDestePc()






