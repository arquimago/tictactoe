# -*- coding: utf-8 -*-
import arvore
from minimax import minimax

def main():

  tabuleiro = [' ']*9
  
  raiz = arvore.No(tabuleiro)

  arvore.geraArvore(tabuleiro,raiz)

  arvore.avaliarArvore(raiz)

  minimax_value = minimax(raiz, 2, True)

  print 'Minimax melhor valor: ' + str(minimax_value)

  for i,filho in enumerate(raiz.filhos):
    if filho.avaliacao == minimax_value:
      print 'Melhor jogada vai para:'
      filho.imprimir()
      break


if __name__ == '__main__': main()
