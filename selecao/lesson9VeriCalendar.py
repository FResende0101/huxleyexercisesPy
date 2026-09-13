#Faça um programa que recebe duas datas distintas e exibe a mais recente, ou seja, aquela que está mais próxima da data atual. 
# Considere apenas datas passadas, isto é, nenhuma das datas representará um momento futuro.

# Cada data deve ser fornecida como três valores inteiros, onde o primeiro representa o dia, o segundo o mês e o terceiro o ano.
# Dica: comece verificando pelo ano, depois pelo mês e, se necessário, por último pelo dia.
# ##
diaDtum, mesDtum, anoDtum = map(int,input().split()) 
diaDtdois, mesDtdois, anoDtdois = map(int,input().split())

if (anoDtum, mesDtum, diaDtum) > (anoDtdois, mesDtdois, diaDtdois):
    print(f"{diaDtum} {mesDtum} {anoDtum}")
else:
     print(f"{diaDtdois} {mesDtdois} {anoDtdois}")

