#[while]
#Um professor precisa saber qual a média das notas de uma sala e pediu sua ajuda para construir um programa que permita inserir
# as notas finais de cada aluno e, ao final, exibir a média da sala. Lembre-se que as notas variam de 0 a 10 e o professor 
# digitará -1 quando quiser encerrar as entradas. 
# Obs.: use variáveis de ponto flutuante de dupla precisão.
# ##

qtdnotas = 0
nota = 0
somanota = 0

while nota != -1:
    nota = float(input())
    if nota != -1:
        qtdnotas += 1
        somanota += nota

medNota = somanota / qtdnotas

print(f"{medNota:.2f}")


