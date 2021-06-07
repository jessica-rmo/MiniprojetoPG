from math import sqrt, acos
# import main

def norma(vetor):
    x1 = vetor.x1
    x2 = vetor.x2
    x3 = vetor.x3

    return sqrt(x1**2 + x2**2 + x3**2)

# vetor1 = main.Vetor(4, 3, 6)
# print(norma(vetor1))

def produtoEscalar(vetor1, vetor2):
    x1 = vetor1.x1
    x2 = vetor2.x1

    y1 = vetor1.x2
    y2 = vetor2.x2

    z1 = vetor1.x3
    z2 = vetor2.x3

    return (x1*x2) + (y1*y2) + (z1*z2)

# vetor2 = main.Vetor(2,-4,-1)
# vetor3 = main.Vetor(0,5,2)

# print(produtoEscalar(vetor2, vetor3))

def cosseno(vetor1, vetor2):
    return acos(produtoEscalar(vetor1, vetor2)/(norma(vetor1) * norma(vetor2)))

# print('Norma 1: ', norma(vetor2))
# print('Norma 2: ', norma(vetor3))
# print('Produto Escalar: ', produtoEscalar(vetor2, vetor3))
# print('Cosseno: ', cosseno(vetor2, vetor3))

def saoParalelos(vetor1, vetor2):
    x = vetor1.x1/vetor2.x1
    y = vetor1.x2/vetor2.x2
    z = vetor1.x3/vetor2.x3

    if(x == y and x == z and y == z):
        return True
    
    return False

# vetor21 = main.Vetor(5, 15, 81)
# vetor22 = main.Vetor(8, 12, 16)

# print(saoParalelos(vetor21, vetor22))