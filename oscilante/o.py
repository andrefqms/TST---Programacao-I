# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Números Oscilantes

def numero_oscilante(entrada):
	diferente = 0
	juntos = 0
	for i in range(len(entrada)-1): 
		if int(entrada[i]) % 3 == 0 and int(entrada[i+1]) %3 != 0:
			diferente += 1
		elif int(entrada[i]) % 2 == 0 and int(entrada[i+1]) % 2 != 0:
			diferente += 1
	
		else:
			juntos += 1
	print juntos
	print diferente
	if juntos > 0:
		return 'verdadeiro'
	elif juntos > 0:
		return 'falso'

entrada = raw_input()

print '%s: %d algarismos.' % (numero_oscilante(entrada),len(entrada))
			
