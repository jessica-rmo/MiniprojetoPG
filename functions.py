from math import *
from Estruturas import *

# Ferramentas Básicas

def produtoEscalar(vetor1, vetor2):
    x1 = vetor1.x1
    x2 = vetor2.x1

    y1 = vetor1.x2
    y2 = vetor2.x2

    z1 = vetor1.x3
    z2 = vetor2.x3

    return (x1*x2) + (y1*y2) + (z1*z2)

def norma(vetor):
    x1 = vetor.x1
    x2 = vetor.x2
    x3 = vetor.x3

    return sqrt(x1**2 + x2**2 + x3**2)

def normalize(vetor):
    n1 = norma(vetor)
    return Vetor(vetor.x1/n1, vetor.x2/n1, vetor.x2/n1)

def cosseno(vetor1, vetor2):
    return acos(produtoEscalar(vetor1, vetor2)/(norma(vetor1) * norma(vetor2)))

def projecao(vetor1, vetor2):
    n1    = produtoEscalar(vetor1, vetor2)
    n2    = produtoEscalar(vetor2, vetor2)
    proj  = n1/n2
    vetor = Vetor(proj*(vetor2.x1), proj*(vetor2.x2), proj*vetor2.x3)
    return vetor

def produtoVetorial(vetor1, vetor2):
    i = (vetor1.x2 * vetor2.x3) - (vetor1.x3 * vetor2.x2)
    j = (vetor1.x3 * vetor2.x1) - (vetor1.x1 * vetor2.x3)
    k = (vetor1.x1 * vetor2.x2) - (vetor1.x2 * vetor2.x1)
    return Vetor(i, j, k)

def saoParalelos(vetor1, vetor2):
    x = vetor1.x1/vetor2.x1
    y = vetor1.x2/vetor2.x2
    z = vetor1.x3/vetor2.x3

    if(x == y and x == z and y == z):
        return True
    
    return False

# Objetos

def diretor(reta):
    v = reta.getVetorDiretor()
    return Vetor(v.x(), v.y(), v.z())

def normal(plano):
    return plano.vetorNormal

def eParalelo(vetor, reta):
    vetorD = reta.getVetorDiretor()
    if norma(vetor) == 0 or norma(vetorD) == 0:
        return True
    else:
        k = vetor.x1 / vetorD.x1
        if (vetor.x2 / vetorD.x2) != k:
            return False
        elif (vetor.x3 / vetorD.x3) != k:
            return False
        return True

def eOrtogonal(vetor, plano):
    ort = produtoEscalar(vetor, plano.vetorNormal)

    if ort == 0:
        return True
    
    return False

def projecao(vetor, reta):
    vetor2 = reta.getVetorDiretor()
    n1     = produtoEscalar(vetor, vetor2)
    n2     = produtoEscalar(vetor2, vetor2)
    proj   = n1/n2
    vetor  = Vetor(proj*(vetor2.x1), proj*(vetor2.x2), proj*vetor2.x3)
    return vetor

def projecao(vetor, plano):
    escalarVN = produtoEscalar(vetor, plano.vetorNormal)
    escalarNN = produtoEscalar(plano.vetorNormal, plano.vetorNormal)
    res = (escalarVN/escalarNN)
    i1 = res*plano.vetorNormal.x1 
    i2 = res*plano.vetorNormal.x2 
    i3 = res*plano.vetorNormal.x3

    return Vetor(vetor.x1 - i1, vetor.x2 - i2, vetor.x3 - i3)

def componenteOrtogonal(vetor, plano):
    n = plano.getVetorNormal()
    proj = projecao(vetor, n)
    comp = Vetor(vetor.x1 - proj.x1, vetor.x2 - proj.x2, vetor.x3 - proj.x3)
    return comp

def formaCartesiana(plano):
    a = plano.vetorNormal.x()
    b = plano.vetorNormal.y()
    c = plano.vetorNormal.z()
    ponto_a = plano.ponto.x()
    ponto_b = plano.ponto.y()
    ponto_c = plano.ponto.z()
    d = -((a*ponto_a) + (b*ponto_b) + (c*ponto_c))
    return [a,b,c,round(d,2)]

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

# Interseções

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
