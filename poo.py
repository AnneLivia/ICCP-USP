class Carro:
    def __init__(self, modelo, ano, cor, maxvel):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.maxvel = maxvel
        self.vel = 0
    
    def imprimir(self):
        if(self.vel == 0): # carro parado
            print("%s %s %d"%(self.modelo, self.cor, self.vel))
        elif self.vel < self.maxvel:
            print("%s %s indo a %d km/h"%(self.modelo, self.cor, self.vel))
        else:
            print("%s %s indo muiiiiito rapidooo!"%(self.modelo, self.cor))
    
    def acelerar(self, velocidade):
        self.vel = velocidade
        if(self.vel > self.maxvel):
            self.vel = self.maxvel
        self.imprimir()
    
    def pare(self):
        self.vel = 0
        self.imprimir()
            
def main():
    carro1 = Carro('brasilia', 1968, 'amarela', 80)
    carro2 = Carro('fuscão', 1981, 'preto', 95)
    carro1.acelerar(40)
    carro2.acelerar(50)
    carro1.acelerar(80)
    carro1.pare()
    carro2.acelerar(100)

main()