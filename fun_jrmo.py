# Funcoes
import Estruturas as e

def formaCartesiana(plano):
    a = plano.vetorNormal.x()
    b = plano.vetorNormal.y()
    c = plano.vetorNormal.z()
    ponto_a = plano.ponto.x()
    ponto_b = plano.ponto.y()
    ponto_c = plano.ponto.z()
    d = -((a*ponto_a) + (b*ponto_b) + (c*ponto_c))
    return [a,b,c,d]

# p = e.Plano(e.Ponto(1,1,-3),e.Vetor(2,3,4))
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

ponto = e.Ponto(-1,-2,1)
vetorDiretor = e.Vetor(-5,13,-8)
reta = e.Reta(ponto,vetorDiretor)
print(reta.equacaoParametrica())
print(formaCartesiana(reta))


# def interseção(reta1, reta2):
#
#     return 0

# ponto = e.Ponto(1, 2, 3)
# vetorDiretor = e.Vetor(2,4,6)
# reta = e.Reta(ponto,vetorDiretor)
# print(reta.equacaoParametrica())
#
# ponto2 = e.Ponto(2.4, 4.8, 7.2)
# vetorDiretor = e.Vetor(-1,3,5)
# reta = e.Reta(ponto2,vetorDiretor)
# print(reta.equacaoParametrica())


# def interseção(reta, plano):

