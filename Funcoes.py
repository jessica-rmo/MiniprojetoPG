from .Estruturas import *
from .fun import *

# funções

# Produto vetorial
# Prjeção vetro em vetor
# Normalização


def produtoVetorial(vetor1, vetor2):
    i = (vetor1.x2 * vetor2.x3) - (vetor1.x3 * vetor2.x2)
    j = (vetor1.x3 * vetor2.x1) - (vetor1.x1 * vetor2.x3)
    k = (vetor1.x1 * vetor2.x2) - (vetor1.x2 * vetor2.x1)
    return Vetor(i, j, k)

#vetor1 = Vetor(1,1,-1)
#vetor2 = Vetor(2,1,4)
#vetor3 = produtoVetorial(vetor1, vetor2)
#print(vetor3.get())

# Projeção de um vetor em outro

def projecao(vetor1, vetor2):
    n1    = produtoEscalar(vetor1, vetor2)
    n2    = produtoEscalar(vetor2, vetor2)
    proj  = n1/n2
    vetor = Vetor(proj*(vetor2.x1), proj*(vetor2.x2), proj*vetor2.x3)
    return vetor

#vetor1 = Vetor(2,3,4)
#vetor2 = Vetor(1,-1,0)
#print(projecao(vetor1, vetor2))

# Faz com que a soma das cordenadas de um vetor seja igual a 1
def normalizacao(vetor):
    n1 = norma(vetor)
    return Vetor(vetor.x1/n1, vetor.x2/n1, vetor.x2/n1)

#vetor = Vetor(2,3,4)
#soma = int(normalizacao(vetor).x1 + normalizacao(vetor).x2 + normalizacao(vetor).x3)
#print(soma)





# Sobre objeto






# Projeção vetor em reta
# eParalelo
# Vetor diretor
# Componentes Ortogonais

# Projeção vetor reta

def projecao(vetor, reta):
    vetor2 = reta.getVetorDiretor()
    n1     = produtoEscalar(vetor, vetor2)
    n2     = produtoEscalar(vetor2, vetor2)
    proj   = n1/n2
    vetor  = Vetor(proj*(vetor2.x1), proj*(vetor2.x2), proj*vetor2.x3)
    return vetor

#vetor = Vetor(2,3,4)
#ponto = Ponto(1,2,3)
#vetorD = Vetor(0,3,-4)
#reta = Reta(ponto, vetorD)
#print(projecao(vetor, reta))


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

#vetor = Vetor(-2,3,4)
#ponto = Ponto(1,2,2)
#vetorD = Vetor(-4,6,8)
#reta = Reta(ponto,vetorD)
#print(eParalelo(vetor, reta))

def vetorDiretor(reta):
    v = reta.getVetorDiretor()
    return Vetor(v.x(), v.y(), v.z())


# ponto = Ponto(1,2,3)
# vetorD = Vetor(4,-5,-7)
# reta = Reta(ponto,vetorD)
# print(vetorDiretor(reta))

def vetorNormal(plano):
    v = plano.getVetorNormal()
    return Vetor(v.x(), v.y(), v.z())

# ponto = Ponto(1,2,3)
# vetorN = Vetor(4,-5,-7)
# plano = Plano(ponto,vetorN)
# print(vetorNormal(plano))


def componenteOrtogonal(vetor, plano):
    n = plano.getVetorNormal()
    proj = projecao(vetor, n)
    comp = Vetor(vetor.x1 - proj.x1, vetor.x2 - proj.x2, vetor.x3 - proj.x3)
    return comp

# v = Vetor(-5, 1, 10)
# ponto = Ponto(1,2,3)
# vetorN = Vetor(1,-3,-2)
# plano = Plano(ponto,vetorN)
# print(componenteOrtogonal(v, plano))