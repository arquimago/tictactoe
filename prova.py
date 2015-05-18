import arvore

def main():

  tabuleiro = [' ']*9
  
  raiz = arvore.No(tabuleiro)

  arvore.geraArvore(tabuleiro,raiz)

  arvore.avaliarArvore(raiz)


if __name__ == '__main__': main()
