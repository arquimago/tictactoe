# -*- coding: utf-8 -*-

from arvore import No
from arvore import final
from avaliacao import avaliacao
#from tictactoe import isWinner

#o tabuleiro é um dos atributos do no, e nao o no em si, e essa funcao vai bugar
#pq o isWinner não lê a posição 0 e vai até 9, meu vetor vai de 0 a 8 :P
#arrumei essa funcao na arvore... 
def isTerminalNode(node):
	return final(node.tabuleiro, 'X') or final(node, 'O')

def minimax(node, depth, maximizingPlayer):
    if depth == 0 or isTerminalNode(node):
        return avaliacao(node)
    if maximizingPlayer:
        bestValue = -9999
        for child in node.filhos:
            val = minimax(child, depth - 1, False)
            bestValue = max(bestValue, val)
        return bestValue
    else:
        bestValue = +9999
        for child in node.filhos:
            val = minimax(child, depth - 1, True)
            bestValue = min(bestValue, val)
        return bestValue
