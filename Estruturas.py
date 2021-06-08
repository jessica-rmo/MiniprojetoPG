# Miniprojeto 0 - Processamento Gráfico 2020.2 CIn UFPE
# Jessica Oliveira (jrmo@cin.ufpe.br)
# Atualizado em 08/06/2021

# Estruturas básicas

class Ponto:
    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

    def x(self):
        return self.x1
    def y(self):
        return self.x2
    def z(self):
        return self.x3
    def get(self): #retorna o ponto como uma lista
        return [self.x1, self.x2, self.x3]
    def __str__(self):
        return "(" + str(self.x1) + ", " + str(self.x2) + " ," + str(self.x3) + ")"

    def __sub__(self, other):
        x = self.x() - other.x()
        y = self.y() - other.y()
        z = self.z() - other.z()
        return Ponto(x,y,z)

# pontoA = Ponto(-1,5,3)
# print(pontoA.x())
# print(pontoA.y())
# print(pontoA.z())
# print(pontoA.get())
# pontoA.print()

class Vetor(Ponto):
    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
    # funcoes herdadas de Ponto:
    # x(), y(), z(), get(), __str__(), __sub()__

# vetor1 = Vetor(1,2,3)
# print(vetor1.x())
# print(vetor1.y())
# print(vetor1.z())
# print(vetor1.get())
# vetor1.print()

class Segmento:
    def __init__(self, ponto1, ponto2):
        self.ponto1 = ponto1
        self.ponto2 = ponto2

    def pontoInicial(self):
        return ponto1
    def pontoFinal(self):
        return ponto2
    def vetorDiretor(self):
        p = (self.ponto2 - self.ponto1)
        return Vetor(p.x(),p.y(),p.z())

# ponto1 = Ponto(1,2,3)
# ponto2 = Ponto(4,-5,-7)
# segmentoAB = Segmento(ponto1,ponto2)
# print(segmentoAB.pontoInicial())
# print(segmentoAB.pontoFinal())
# print(segmentoAB.vetorDiretor())

class Reta:
    def __init__(self, ponto, vetorDiretor):
        self.ponto = ponto
        self.vetorDiretor = vetorDiretor

    def equacaoParametrica(self):
        matrix = [["x = ",(self.ponto.x()),(self.vetorDiretor.x()),"t"],
                  ["y = ",(self.ponto.y()),(self.vetorDiretor.y()),"t  , t pertence a R"],
                  ["z = ",(self.ponto.z()),(self.vetorDiretor.z()),"t"]]
        forma = ""
        for line in matrix:
            for i in line:
                if line.index(i) == 2 and i < 0 and line[1] != 0:
                    forma = forma + " - " + str(abs(i))
                elif line.index(i) == 2 and i > 0 and line[1] != 0:
                    forma = forma + " + " + str(abs(i))
                elif (i == 0):
                    forma = forma
                else:
                    forma = forma + str(i)
            if (matrix.index(line) < 2):
                forma = forma + "\n"
            forma = forma
        return forma

    def vetorDiretor(reta):
        v = reta.getVetorDiretor()
        return Vetor(v.x(), v.y(), v.z())

    
# ponto = Ponto(1,2,3)
# # vetorDiretor = Vetor(4,-5,-7)
# # reta = Reta(ponto,vetorDiretor)
# # print(reta.equacaoParametrica())

class Plano:
	def __init__(self, ponto, vetorNormal):
		self.ponto = ponto
		self.vetorNormal = vetorNormal

# plano = Plano(Ponto(1,1,0),Vetor(2,3,4))
# print(plano.ponto)
# print(plano.vetorNormal)

class Esfera:
    origem = Ponto(0,0,0)
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = abs(raio)

    def equacao(self):
        if (self.centro == self.origem):
            return "x^2 + y^2 + z^2 = " + str(self.raio**2)
        else:
            x0 = -self.centro.x()
            y0 = -self.centro.y()
            z0 = -self.centro.z()
            if   (x0 > 0): x0 = " + " + str(x0)
            elif (x0 < 0): x0 = " - " + str(abs(x0))
            else: x0 = ""

            if   (y0 > 0): y0 = " + " + str(y0)
            elif (y0 < 0): y0 = " - " + str(abs(y0))
            else: y0 = ""

            if   (z0 > 0): z0 = " + " + str(z0)
            elif (z0 < 0): z0 = " - " + str(abs(z0))
            else: z0 = ""

            return "(x" + str(x0) + ")^2 + (y" + str(y0) + ")^2 + (z" + str(z0) + ")^2 = " + str(self.raio**2)

# esferaA = Esfera(Ponto(5,-1,4), 6)
# print(esferaA.centro)
# print(esferaA.raio)
# print(esferaA.equacao())

class Triangulo:
    def __init__(self, ponto1, ponto2, ponto3):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
        self.ponto3 = ponto3

class Base:
    def __init__(self, v1, v2, v3):
        self.vetor1 = v1
        self.vetor2 = v2
        self.vetor3 = v3

    def __str__(self):
        return "Bases: " + str(self.vetor1) + ", " + str(self.vetor2) + ", " + str(self.vetor3)

# v1=Vetor(1,2,3)
# v2=Vetor(9,-2,7)
# v3=Vetor(0,4,-1)
# baseB = Base(v1,v2,v3)
# print(baseB)
