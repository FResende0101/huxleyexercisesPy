#[for] Desenvolva um programa que exibe a tabuada de um número natural escolhido pelo usuário. 
# Os múltiplos apresentados devem ser de 1 a 10.

numero = int(input())
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

