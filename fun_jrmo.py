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
    return [a,b,c,round(d,2)]

# p = Plano(Ponto(1,1,-3),Vetor(2,3,4))
# print(formaCartesiana(p))


def intersecao(plano1,plano2):
    p1 = formaCartesiana(plano1)
    a, b, c, d = p1[0], p1[1], p1[2], p1[3]
    p2 = formaCartesiana(plano2)
    e, f, g, h = p2[0], p2[1], p2[2], p2[3]
    i = round(a/e,2)
    j = round(b/f,2)
    k = round(c/g,2)
    l = -round(d/h,2)

    # i = round(a / 8, 2)
    # j = round(b / -10, 2)
    # k = round(c / -3, 2)
    # l = -round(d / 19, 2) #concidentes
    # l = -round(d / 15, 2) #nao conscidentes

    if (saoParalelos(plano1.vetorNormal,plano2.vetorNormal)):
        if(i==j and j==k and k==i and i==l): # coincidentes
            return plano1
        else: # nao coincidentes
            return None
    else:
        return "doing"

plano1 = Plano(Ponto(2,0,-1),Vetor(-4,5,1.5))
plano2 = Plano(Ponto(1.04,5.71,1.2),Vetor(0.91,4.6,6))
print(intersecao(plano1,plano2))


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
            return None
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

    return [[round(y0/x0,2), -1,  0, round(b-((a*y0)/x0),2)],
            [round(z0/x0,2),  0, -1, round(c-((a*z0)/x0),2)] ]

# ponto = Ponto(2,-5.2,3.2)
# vetorDiretor = Vetor(-5,13,-8)
# reta = Reta(ponto,vetorDiretor)
# print(formaCartesiana(reta))


def intersecao(reta1, reta2):
    A = reta1.ponto
    vdA = reta1.getVetorDiretor()
    vdB = reta2.getVetorDiretor()

    eqB = formaCartesiana(reta2)  # [[a,b,c,d],[e,f,g,h]]
    print(str(reta2.getVetorDiretor()))
    a, b, c, d = eqB[0][0], eqB[0][1], eqB[0][2], eqB[0][3]
    e, f, g, h = eqB[1][0], eqB[1][1], eqB[1][2], eqB[1][3]
    print(str(eqB))
    x, y, z = A.x(), A.y(), A.z()
    # vetores da eqs da forma cartesiana da reta2
    v1B = Vetor(a,b,c)
    v2B = Vetor(e,f,g)

    # t1 e t2 das eqs da forma castesiana da reta2 com ponto A da reta1
    t1 = -round((produtoEscalar(A,v1B) + d)/(produtoEscalar(vdA,v1B)),2)
    t2 = -round((produtoEscalar(A,v2B) + h)/(produtoEscalar(vdA,v2B)),2)

    if ( t1 == t2 ): # existe intersecao
        if (saoParalelos(vdA,vdB)): # vetores diretores das 2 retas
            return reta1 #ou reta2
        else: #retornar ponto da intersecao
            p = x + vdA.x()*t1
            q = y + vdA.y()*t1
            r = z + vdA.z()*t1
            return Ponto(round(p,2),round(q,2),round(r,2))
    else: # nao existe intersecao
        return None

# ponto = Ponto(1, 2, 3)
# vetorDiretor = Vetor(2,4,6)
# reta1 = Reta(ponto,vetorDiretor)
# ponto2 = Ponto(-1,3,5)
# vetorDiretor = Vetor(3.4,1.8,2.2)
# reta2 = Reta(ponto2,vetorDiretor)
#
# inter = intersecao(reta1,reta2)
# print(str(inter))
