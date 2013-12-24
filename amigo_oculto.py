#coding: utf-8
# Programa em Python para sortear os participantes do amigo oculto entre si.

# Passo 1: Ler um arquivo com os dados dos participantes;
""" ID(int)  Nome(string)  Email(string)  Sugestões_de_presentes(string)
  Restrições(CSV, int)
"""
import csv
import sys

# variables
mainList = []		# contains the data
labels = []			# contains the headers of each column on csv
i=0

f = open(sys.argv[1], 'rb') # opens the csv file
try:
  reader = csv.reader(f) 		# creates the reader object
  for row in reader:		  	# iterates the rows of the file in orders
  	if i!=0:
  		mainList.append(row)
  	else:
  		labels.append(row)
  	print row 							# prints each row
  	i+=1
finally:
  f.close()      						# closing

print "---"
print "Labels:"
print labels
print "My list:"
mainList.sort(key=lambda position: position[3])
# doing: alphabetic sort of restrictions
# TODO: sort by number of restrictions...
print mainList

"""
 Reordenar lista para sortear primeiro os participantes que possuem mais
 restrições
"""


# Passo 2: Fazer sorteio, retirando os números sorteados da lista;
""" Observar as restrições:
    - não pode sair consigo mesmo;
    - não pode sair com alguém que está na sua lista de restrições;
"""

# Passo 3: Enviar email para os participantes com o amigo a ser presenteado;