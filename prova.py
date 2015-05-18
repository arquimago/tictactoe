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

  print 'Minimax resultado: ' + str(minimax(raiz, 2, True))



if __name__ == '__main__': main()
