#[while] Elabore um programa que recebe valores inteiros até que seja digitado o valor zero. 
# O programa deverá exibir a média aritmética dos valores recebidos. 
# Lembre-se: o valor zero apenas sinaliza o fim da entrada, não deve ser contabilizado.
#Obs.: Não existe média sem que pelo menos um valor seja dado antes do zero, portanto neste problema ESTÁ GARANTIDO QUE HÁ MÉDIA.
# #

acumulador = 0
contador = 0
enterValores = int(input())
#preciso de uma forma de entrar 0 sem influenciar na repetição alem de interrompe-la


while enterValores !=0:
        acumulador += enterValores
        contador += 1 
        enterValores = int(input())
mediavalores = acumulador/contador


print(f"{mediavalores:.0f}")
