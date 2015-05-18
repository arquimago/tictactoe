# -*- coding: utf-8 -*-

from arvore import No
from avaliacao import avaliacao
from tictactoe import isWinner

def isTerminalNode(node):
	return isWinner(node, 'X') or isWinner(node, 'O')

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