# -*- coding: utf-8 -*-
import arvore
from minimax import minimax

def main():

  print "Terceira questao"
  tabuleiro = [' ']*9
  raiz = arvore.No(tabuleiro)
  print " "
  arvore.geraArvore(tabuleiro,raiz)
  print "Abaixo segue a arvore, com nos raiz, filhos e netos"
  print " "
  arvore.imprimirArvore(raiz)
  print " "
  print "Avaliacao das folhas"
  arvore.avaliarArvore(raiz)

  print " "
  
  minimax_value = minimax(raiz, 2, True)

  print 'Minimax melhor valor: ' + str(minimax_value)

  for i,filho in enumerate(raiz.filhos):
    if filho.avaliacao == minimax_value:
      print 'Melhor jogada vai para:'
      filho.imprimir()
      break



if __name__ == '__main__': main()
