# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Soma e Diminui Vizinhos!

def soma_diminui_vizinhos(lista):
	if lista == []:
		return 0
	
	resultado = lista[0]

	for i in range(1, len(lista)):
		if i % 2 == 0:
			resultado -= lista[i]
		else:
			resultado += lista[i]
	return resultado


lista = [1,2,3]	

assert soma_diminui_vizinhos(lista) == 0
