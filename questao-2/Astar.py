#!/usr/bin/python


import heapq
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
	'E' : [],
	'F' : [],
	'G' : []
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
custo_final = 0
finished = False
openset = []
closedset = []
heapq.heappush(openset, (h[start],start,None))

while not finished:
    no_atual = []
    no_atual = heapq.heappop(openset)
    if no_atual[1] not in nos_expandidos:
        nos_expandidos.append(no_atual[1])
    if no_atual[1] not in closedset:
        closedset.append([no_atual[1],no_atual[2]])
    if no_atual[1] == finish:
        finished = True
        custo_final = no_atual[0]
    
    adjacentes = grafo2[no_atual[1]]
    for no, custo in adjacentes:
        if no not in nos_expandidos:
            custo += no_atual[0] - h[no_atual[1]] + h[no]
            heapq.heappush(openset, (custo,no,no_atual[1]))
            
end = closedset[-1]
father = end[1]
path = []
path.append(end[0])
while father != None:
    for no, pai in reversed(closedset):
        if no == father:
            father = pai
            path.append(no)
path.reverse()


print 'NOS EXPANDIDOS'
print nos_expandidos
print 'CAMINHO DA SOLUCAO'
print path
print 'CUSTO DO CAMINHO DA SOLUCAO'
print custo_final

