from math import *
from Estruturas import *

# Funções Básicas

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


def saoParalelos(vetor1, vetor2):
    x = vetor1.x1/vetor2.x1
    y = vetor1.x2/vetor2.x2
    z = vetor1.x3/vetor2.x3

    if(x == y and x == z and y == z):
        return True
    return False

def saoOrtogonais(vetor1, vetor2):
    x = fun.produtoEscalar(vetor1, vetor2)
    if (x == 0):
        return True
    else:
        return False

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


# def intersecao(reta,triangulo):


def intersecao(plano1,plano2):
    p1 = formaCartesiana(plano1)
    a, b, c, d = p1[0], p1[1], p1[2], p1[3]
    p2 = formaCartesiana(plano2)
    e, f, g, h = p2[0], p2[1], p2[2], p2[3]
    i = round(a/e,2)
    j = round(b/f,2)
    k = round(c/g,2)
    l = -round(d/h,2)

    if (saoParalelos(plano1.vetorNormal,plano2.vetorNormal)):
        if(i==j and j==k and k==i and i==l): # coincidentes
            return plano1
        else: # nao coincidentes
            return None
    else:
        # Vetor diretor da reta intersecao dos planos
        vetorDiretor = produtoVetorial(plano1.vetorNormal,plano2.vetorNormal)

        # Ponto que pertence a reta
        Px = 0   # Px = round(((c*h)-(g*d))/((g*a)-(c*e)),2)
        Py = round(((c*h)-(g*d))/((g*b)-(c*f)),2)
        Pz = round(((b*h)-(f*d))/((f*c)-(b*g)),2)
        ponto = Ponto(Px,Py,Pz)

        reta = Reta(ponto,vetorDiretor)
        return reta

