#Faça um programa que recebe a idade de um nadador e exibe a categoria que ele pertence. 
# Sendo o critério: "infantil" (0 a 10 anos); "junior" (11 a 14 anos); "adolescente" (15 a 20 anos); 
# "jovem" (21 a 35 anos) e; "master" (> 35 anos). 

idade = int(input())

if idade <= 10:
    print("infantil")
elif idade <= 14:
    print("junior")
elif idade <= 20:
    print("adolescente")
elif idade <= 35:
    print("jovem")
else:
    print("master")

