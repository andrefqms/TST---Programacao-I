# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Merge

def merge(lista1,lista2):
	lista3 = lista1 + lista2
	print lista3
	for i in range(len(lista3)-1,0,-1):
		if lista3[i] < lista3[i-1]:
			lista3[i],lista3[i-1] = lista3[i-1],lista3[i]	
			print lista3
	
	return lista3



l1 = [3,7,9,11,14]
l2 = [2,4,10,11,13,19,21,43]
print merge(l1,l2) 
