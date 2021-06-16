import Estruturas
import fun
import Funcoes
import math


def saoOrtogonais(vetor1, vetor2):
    x = fun.produtoEscalar(vetor1, vetor2)
    if (x == 0):
        return True
    else:
        return False


# vetor1 = Estruturas.Vetor(5,0,-3)
# vetor2 = Estruturas.Vetor(0,0,0)

# print (saoOrtogonais(vetor1, vetor2))

def reflexao(vetor1, vetor2):
    x1 = vetor1.x1
    x2 = vetor2.x1

    y1 = vetor1.x2
    y2 = vetor2.x2

    z1 = vetor1.x3
    z2 = vetor2.x3
    # Reflexao na origem:
    if (x2 == 0 and y2 == 0 and z2 == 0):
        return Estruturas.Vetor(x1 * -1, y1 * -1, z1 * -1)
    # reflexao x2=y2=z2
    elif (x2 == y2 and y2 == z2):
        return Estruturas.Vetor(y1, x1, z1)
    # reflexao y2 == 0
    elif (y2 == 0):
        return Estruturas.Vetor(x1 * -1, y1, z1)
    # reflexao x2 == 0
    elif (x2 == 0):
        return Estruturas.Vetor(x1, y1 * -1, z1)
    else:
        return Estruturas.Vetor(x1, y1, z1)


# vetor2 = Estruturas.Vetor(2, -4, -1)
# vetor3 = Estruturas.Vetor(0, 0, 0)
# print(reflexao(vetor2, vetor3))

def eLI(array):
    vetor1 = array[0]
    vetor2 = array[1]
    vetor3 = array[2]

    x1 = vetor1.x1
    x2 = vetor2.x1
    x3 = vetor3.x1

    y1 = vetor1.x2
    y2 = vetor2.x2
    y3 = vetor3.x2

    z1 = vetor1.x3
    z2 = vetor2.x3
    z3 = vetor3.x3

    aux = ((x1 * y2 * z3) + (y1 * z2 * x3) + (z1 * x2 * y3) + (-1 * ((x3 * y2 * z1) + (y3 * z2 * x1) + (z3 * x2 * y1))))

    if (aux != 0):
        return True

    else:
        return False


# vetor1 = Estruturas.Vetor(2, 1, -3)
# vetor2 = Estruturas.Vetor(1, 0, 2)
# vetor3 = Estruturas.Vetor(2, 1, -1)
# array = np.array([vetor1,vetor2,vetor3])
# print(eLI(array))

def saoComplementosOrtogonais(reta, plano):
    vetorDiretor = reta.vetorDiretor
    normalplano = plano.vetorNormal

    x1 = vetorDiretor.x1
    x2 = normalplano.x1

    y1 = vetorDiretor.x2
    y2 = normalplano.x2

    z1 = vetorDiretor.x3
    z2 = normalplano.x3
    if (x1 == 0 and y1 == 0 and z1 == 0 or x2 == 0 and y2 == 0 and z2 == 0):
        return True
    elif (x1 / x2 == y1 / y2 and y1 / y2 == z1 / z2):
        return True
    else:
        return False


# ponto = Estruturas.Ponto(1, 2, 3)
# vetorDiretor = Estruturas.Vetor(2, 3, 4)
# reta = Estruturas.Reta(ponto, vetorDiretor)
# plano = Estruturas.Plano(Estruturas.Ponto(1, 1, 0), Estruturas.Vetor(2, 3, 4))
# print(saoComplementosOrtogonais(reta, plano))


def saoComplementosOrtogonais(plano, reta):
    vetorDiretor = reta.vetorDiretor
    normalplano = plano.vetorNormal

    x1 = vetorDiretor.x1
    x2 = normalplano.x1

    y1 = vetorDiretor.x2
    y2 = normalplano.x2

    z1 = vetorDiretor.x3
    z2 = normalplano.x3
    if (x1 == 0 and y1 == 0 and z1 == 0 or x2 == 0 and y2 == 0 and z2 == 0):
        return True
    elif (x2 / x1 == y2 / y1 and y2 / y1 == z2 / z1):
        return True
    else:
        return False


# ponto = Estruturas.Ponto(1, 2, 3)
# vetorDiretor = Estruturas.Vetor(2, 3, 4)
# reta = Estruturas.Reta(ponto, vetorDiretor)
# plano = Estruturas.Plano(Estruturas.Ponto(1, 1, 0), Estruturas.Vetor(0, 1, 0))
# rint(saoComplementosOrtogonais(plano, reta))


def intersecão(reta, esfera):  # reta - esfera
    pontoR = reta.ponto
    pontoE = esfera.centro

    x1 = pontoR.x1
    x2 = pontoE.x1

    y1 = pontoR.x2
    y2 = pontoE.x2

    z1 = pontoR.x3
    z2 = pontoE.x3

    vetorPC = Estruturas.Vetor(x2 - x1, y2 - y1, z2 - z1)
    vetordiretorR = reta.vetorDiretor
    # precisamos fazer a projecao de vetorPC em vetor diretor da reta
    n1 = fun.produtoEscalar(vetorPC, vetordiretorR)
    n2 = fun.produtoEscalar(vetordiretorR, vetordiretorR)
    proj = n1 / n2
    vetor = Estruturas.Vetor(proj * (vetordiretorR.x1), proj * (vetordiretorR.x2), proj * vetordiretorR.x3)
    vetorProjecao = vetor

    # procurando o cateto oposto D
    D = math.sqrt(fun.norma(vetorPC) ** 2 - fun.norma(vetorProjecao) ** 2)
    # sabendo que o raio eh dado por:
    raio = esfera.raio
    # separando os valores de X Y Z do vetor diretor:
    x3 = vetordiretorR.x1
    y3 = vetordiretorR.x2
    z3 = vetordiretorR.x3
    # separando as possibilidades
    #pegando os produtos escalar
    PEvv = fun.produtoEscalar(vetordiretorR, vetordiretorR)
    PEpp = fun.produtoEscalar(vetorPC, vetorPC)
    PEvp = fun.produtoEscalar(vetordiretorR, vetorPC)
    if (D == raio):
        # uma intersecao
        t = PEvp / PEvv
        pontointer = (x1 + (x3 * t), (y1 + (y3 * t)), (z1 + (z3 * t)))
        return pontointer

    elif (D < raio):
        # duas intersecoes
        # primeiro ponto
        t1 = (PEvp + math.sqrt(PEvp**2-PEvv*PEpp-(raio)**2))/PEvv
        pontointer1 = (x1 + (x3 * t1), (y1 + (y3 * t1)), (z1 + (z3 * t1)))
        # segundo ponto
        t2 = (PEvp - math.sqrt(PEvp ** 2 - PEvv * PEpp - (raio) ** 2)) / PEvv
        pontointer2 = (x1 + (x3 * t2), (y1 + (y3 * t2)), (z1 + (z3 * t2)))
        return pontointer1, pontointer2