import arvore
from minimax import minimax

def main():

  tabuleiro = [' ']*9
  
  raiz = arvore.No(tabuleiro)

  arvore.geraArvore(tabuleiro,raiz)

  arvore.avaliarArvore(raiz)

  print 'Minimax resultado: ' + str(minimax(raiz, 2, True))


if __name__ == '__main__': main()
