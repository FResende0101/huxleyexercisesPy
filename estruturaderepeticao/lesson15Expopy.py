numero = float(input())
expoente = int(input())
acum = 1 #apos erro em relação ao teste com expoente 0. Qual qualquer número multiplicado por 1 permanece ele mesmo ao iniciar
         #e também:range(expoente): O laço executará exatamente expoente vezes (se for 0, roda 0 vezes e mantém acum = 1.0).

for i in range(expoente):
    acum *=  numero


print(f"{acum:.2f}")