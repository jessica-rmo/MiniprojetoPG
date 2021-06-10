# Funcoes
from Estruturas import *
from fun import *

def formaCartesiana(plano):
    a = plano.vetorNormal.x()
    b = plano.vetorNormal.y()
    c = plano.vetorNormal.z()
    ponto_a = plano.ponto.x()
    ponto_b = plano.ponto.y()
    ponto_c = plano.ponto.z()
    d = -((a*ponto_a) + (b*ponto_b) + (c*ponto_c))
    return [a,b,c,d]

# p = Plano(Ponto(1,1,-3),Vetor(2,3,4))
# print(formaCartesiana(p))


def formaCartesiana(reta):
    a = reta.ponto.x()
    b = reta.ponto.y()
    c = reta.ponto.z()
    x0 = reta.vetorDiretor.x()
    y0 = reta.vetorDiretor.y()
    z0 = reta.vetorDiretor.z()

    if (x0 == 0): x0 = 1
    if (y0 == 0): y0 = 1
    if (z0 == 0): z0 = 1

    return [[y0/x0, -1,  0, b-((a*y0)/x0)],
            [z0/x0,  0, -1, c-((a*z0)/x0)] ]

# ponto = Ponto(-1,-2,1)
# vetorDiretor = Vetor(-5,13,-8)
# reta = Reta(ponto,vetorDiretor)
# print(reta.equacaoParametrica())
# print(formaCartesiana(reta))


# def intersecao(reta1, reta2):
#     ponto1 = reta1.ponto
#     ponto2 = reta2.ponto
#
#     return 0

# ponto = Ponto(1, 2, 3)
# vetorDiretor = Vetor(2,4,6)
# reta = Reta(ponto,vetorDiretor)
# print(reta.equacaoParametrica())
#
# ponto2 = Ponto(2.4, 4.8, 7.2)
# vetorDiretor = Vetor(-1,3,5)
# reta = Reta(ponto2,vetorDiretor)
# print(reta.equacaoParametrica())


def intersecao(reta, plano):
    coef = formaCartesiana(plano)
    a, b, c, d = coef[0], coef[1], coef[2], coef[3]
    x = reta.ponto.x()
    y = reta.ponto.y()
    z = reta.ponto.z()
    x0 = reta.vetorDiretor.x()
    y0 = reta.vetorDiretor.y()
    z0 = reta.vetorDiretor.z()
    prodvRetaPlano = produtoEscalar(reta.vetorDiretor,plano.vetorNormal)
    if (prodvRetaPlano == 0):
        if ( ((a*x)+(b*y)+(c*z)+d) == 0 ):
            return reta
        else:
            return Null
    else:
        t = -((produtoEscalar(reta.ponto,plano.vetorNormal)+d) / prodvRetaPlano)
        xp = x + (x0*t)
        yp = y + (y0*t)
        zp = z + (z0*t)
        return Ponto(round(xp,2),round(yp,2),round(zp,2))

# plano = Plano(Ponto(-3.78,-0.56,3.44),Vetor(1,2,2))
# reta = Reta(Ponto(1,3.3,3.38),Vetor(5.2,4,2.4))
# inter_retaPlano = intersecao(reta,plano)
# print(inter_retaPlano)
