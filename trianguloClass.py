class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimetro(self):
        return self.a + self.b + self.c
    def tipo_lado(self):
        if (self.a == self.b) and (self.a != self.c) or (self.a == self.c) and (self.a != self.b) or (self.c == self.b) and (self.b != self.a):
            return "isósceles"
        elif (self.a == self.b and self.a == self.c):
            return "equilátero"
        else:
            return "escaleno"
    def retangulo(self):
        if self.a > self.b and self.a > self.c:
            h = self.a
            c1 = self.b
            c2 = self.c
        elif self.b > self.a and self.b > self.c:
            h = self.b
            c1 = self.a
            c2 = self.c
        else:
            h = self.c
            c1 = self.a
            c2 = self.b

        if (h ** 2) == ((c1 ** 2) + (c2 ** 2)):
            return True
        else:
            return False
    def semelhantes(self, triangulo):
        if((self.a * 2) == triangulo.a) or (self.a == (triangulo.a * 2)) and ((2 * triangulo.b) == self.b) or ((2 * self.b) == triangulo.b) and ((2 * triangulo.c) == self.c) or ((2 * self.c) == triangulo.c):
            return True
        elif(self.a == triangulo.a and self.b == triangulo.b and self.c == triangulo.c):
            return True
        else:
            return False
def main():
    t = Triangulo(3,4,5)
    t2 = Triangulo(3,4,5)
    print("Retangulo: ", t.retangulo())
    print("Tipo de triângulo: ", t.tipo_lado())
    print("t == t2 ?", t.semelhantes(t2))

    # print("%d %d %d: perimetro: %d"%(t.a,t.b,t.c,t.perimetro()))