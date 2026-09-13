#Faça um programa que recebe o valor de três arestas (número inteiro) e exibe uma mensagem indicando se podem formar um triângulo.
# Em caso afirmativo, indique se ele é equilátero, isósceles ou escaleno.
#Lembre-se: Para que um triângulo exista, a medida de qualquer um dos lados deve ser menor que a soma das medidas dos outros dois.
# 

arestaP = int(input())
ArestaS = int(input())
ArestaT = int(input())

if (arestaP + ArestaS > ArestaT) and (arestaP + ArestaT > ArestaS) and (ArestaS + ArestaT > arestaP):
    print("podem formar um triangulo")
    if arestaP == ArestaS == ArestaT:
        print("equilatero")#todas as arestas são iguais
    elif arestaP != ArestaS and arestaP != ArestaT and ArestaS != ArestaT:
        print("escaleno")#todas as arestas são diferente
    else:
        print("isosceles")#uma das arestas é diferente
else:
    print("nao podem formar um triangulo")