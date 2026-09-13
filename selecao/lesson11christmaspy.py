#Uma empresa decide presentear seus funcionários com um bônus de Natal. O valor é definido como segue: 
#(a) 20% do salário para os funcionários homens com mais de quinze anos de casa;
#(b) 25% do salário para as funcionárias mulheres com mais de dez anos de casa;
#(c) R$ 200,00 para os demais que não se encaixaram nas categorias anteriores. 
#Elabore um programa que recebe o sexo, o tempo de casa e o salário de um funcionário e exibe o valor total que o funcionário receberá
# no Natal (salário + bônus).

sexoFunc = input()
tempoServFunc = int(input())
salarioFunc = float(input())

if  sexoFunc == "h" and tempoServFunc > 15:
    salarioFunc *= 1.20
elif sexoFunc == "m" and tempoServFunc > 10:
    salarioFunc *= 1.25
else:
    salarioFunc += 200

print(f"{salarioFunc:.2f}")