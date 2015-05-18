#!/usr/bin/python
from operator import itemgetter

'''
Grafo como conjunto de arestas
grafo = [('S', 'A', 2),
		('S', 'B', 3),
		('A', 'C', 2),
		('B', 'C', 4),
		('B', 'G', 6),
		('C', 'E', 4),
		('C', 'D', 2),
		('D', 'F', 2)]
'''


grafo2 = {
	'S' : [('A', 2), ('B', 3)],
	'A' : [('C', 2)],
	'B' : [('G', 6), ('C', 4)],
	'C' : [('E', 4), ('D', 2)],
	'D' : [('F', 2)],
	'E' : None,
	'F' : None,
	'G' : None
}

def get_custo_adjacente(no_origem, no_destino):
	adjacentes = grafo2[no_origem]
	for no in adjacentes:
		if no[0] == no_destino:
			return no[1]
	return -1

h = {
	'S' : 5,
	'A' : 3,
	'B': 4,
	'C': 3,
	'D' : 2,
	'E' : 1,
	'F' : 0,
	'G' : 0
}

start = 'S'
finish = 'F'
nos_expandidos = []
solucao = []
custo = 0
finished = False

no_atual = start

#print sorted(grafo2[no_atual], key=itemgetter(1))

while not finished:
	#print no_atual
	if not no_atual in nos_expandidos:
		nos_expandidos.append(no_atual)
	if not no_atual in solucao:
		solucao.append(no_atual)
	adjacentes = grafo2[no_atual]
	best = 99999
	if adjacentes != None:
		adjacentes = sorted(grafo2[no_atual], key=itemgetter(1))
		achou_no = False
		while not achou_no:
			for no in adjacentes:
				if no[0] in nos_expandidos:
					pass
				else:
					if h[no[0]] < best:
						best = h[no[0]]
						custo += no[1]
						no_atual = no[0]
						finished = no_atual == finish
						achou_no = True
					break
			if not achou_no:
				finished = True
	else:
		finished = True

if finished:
	nos_expandidos.append(no_atual)
	solucao.append(no_atual)


print 'NOS EXPANDIDOS: '
print nos_expandidos
print 'SOLUCAO'
print solucao
print 'CUSTO'
print custo