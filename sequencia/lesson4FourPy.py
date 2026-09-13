#A média ponderada é um cálculo matemático que acha o valor médio de um conjunto de números, dando importâncias diferentes (pesos) para cada valor.
#Calcular cada nota multiplando-a de acordo com seu peso, somando os resultados e dividindo pela soma dos pesos.

notaMateriaum = float(input())
pesoMateriaum = 2
notaMateriadois = float(input())
pesoMateriadois = 3

mediaPonderada = ((notaMateriaum * pesoMateriaum) + (notaMateriadois * pesoMateriadois)) / (pesoMateriadois+pesoMateriaum)

print(f"{mediaPonderada:.2f}") 