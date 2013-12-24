#coding: utf-8
# Programa em Python para sortear os participantes do amigo oculto entre si.

# Passo 1: Ler um arquivo com os dados dos participantes;
""" ID(int)  Nome(string)  Email(string)  Sugestões_de_presentes(string)
  Restrições(CSV, int)
"""
import csv
import sys
#from person import Person

# variables
mainList = []		# contains the data
labels = []			# contains the headers of each column on csv
i=0

print "\nFile content:"
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
print "Done reading, closed file\n"

"""
print "---"
print "Labels:"
print labels

x=0
for k in mainList:
  for j in k:
    if len(j)==0:
      x=0
    else:
      x=len(j.split(', '))
    print j, len(j), x
"""

"""
 Reordenar lista para sortear primeiro os participantes que possuem mais
 restrições
"""

# Sorts by number of restrictions, but empty restrictions preceeds single
# restrictions and need to be corrected manually.
mainList.sort(key=lambda position:len(position[-1].split(', ')), reverse=True)

# Changes blank restrictions to last positions.
blankList=[]
for subList in mainList:
  if len(subList[-1]) == 0:
    blankList.append(subList)
    mainList.remove(subList)

for l in blankList:
  mainList.append(l)


print "My list:"
for l in mainList:
  print l
print "end of file..."

"""
params = []
for label in labels:
#  print label
  for att in label:
    print att

#candidate = Person()
"""


# Passo 2: Fazer sorteio, retirando os números sorteados da lista;
""" Observar as restrições:
    - não pode sair consigo mesmo;
    - não pode sair com alguém que está na sua lista de restrições;
"""



# Passo 3: Enviar email para os participantes com o amigo a ser presenteado;

