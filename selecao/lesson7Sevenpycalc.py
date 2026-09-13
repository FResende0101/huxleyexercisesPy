print("1: adicao / 2: subtracao / 3: multiplicacao / 4: divisao")
operador = int(input())
numPrimeiro = float(input())
numSegundo = float(input())

if operador == 1:
    resultado = numPrimeiro + numSegundo
    operacao = "adicao"
elif operador == 2:
    resultado = numPrimeiro - numSegundo
    operacao = "subtracao"
elif operador == 3:
    resultado = numPrimeiro * numSegundo
    operacao = "multiplicacao"
elif operador == 4:
    resultado = numPrimeiro / numSegundo
    operacao = "divisao"

print(f"A {operacao} eh: {resultado:.2f}")

#calculadora com 4 operadores
