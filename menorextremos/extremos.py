## coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Classifica Números pelo Menor dos Extremos

n = int(raw_input())
lista = []
y = 0
w = 0

for i in range(n):
    numero = int(raw_input())
    lista.append(numero)

if lista[0] > lista[len(lista)-1]:
    for i in range(len(lista)):
        y = y + 1
    print "Menor dos extremos: %d" % y 

elif lista[0] < lista[len(lista)-1]:
    for i in range(len(lista)):
        y = y + 1
    print "Menor dos extremos: %d" % y

for i in range(len(lista)):
    if y > lista[i]:
        w = w + 1
print "%d número(s) abaixo do menor" % w

for i in range(len(lista)):
    if y < lista[i]:
        w = w + 1
print "%d número(s) acima do menor" % w 
