def imprimir(tabuleiro):
  print ' '
  print '   |   |'
  print ' ' + tabuleiro[0] + ' | ' + tabuleiro[1] + ' | ' + tabuleiro[2]
  print '___|___|____'
  print '   |   |'
  print ' ' + tabuleiro[3] + ' | ' + tabuleiro[4] + ' | ' + tabuleiro[5]
  print '___|___|____'
  print '   |   |'
  print ' ' + tabuleiro[6] + ' | ' + tabuleiro[7] + ' | ' + tabuleiro[8]
  print '   |   |'

def copiar(tab):
  tabTemp = []
  for celula in tab:
    tabTemp+=celula
  return tabTemp

def rodar(tab):
  tabuleiro=[]
  tabuleiro+=tab[2]
  tabuleiro+=tab[5]
  tabuleiro+=tab[8]
  tabuleiro+=tab[1]
  tabuleiro+=tab[4]
  tabuleiro+=tab[7]
  tabuleiro+=tab[0]
  tabuleiro+=tab[3]
  tabuleiro+=tab[6]
  return tabuleiro

def espelhar(tab):
  tabuleiro=[]
  tabuleiro+=tab[2]
  tabuleiro+=tab[1]
  tabuleiro+=tab[0]
  tabuleiro+=tab[5]
  tabuleiro+=tab[4]
  tabuleiro+=tab[3]
  tabuleiro+=tab[8]
  tabuleiro+=tab[7]
  tabuleiro+=tab[6]
  return tabuleiro  

def igual(tab1,tab2):
  for i in range(0,9):
    if tab1[i]!=tab2[i]:
	  return False
  return True

def simetrico(tab1,tab2):
  for i in range(0,4):
    if igual(tab1,tab2):
      return True
    tab2 = espelhar(tab2)
    if igual(tab1,tab2):
	  return True
    tab2 = espelhar(tab2)
    tab2 = rodar(tab2)
  return False

def gerarArvore():
  arvore=[]
  tabuleiro = [' ']*9
  tabuleiro[0]='X'
  arvore+=[copiar(tabuleiro)]
  tabuleiro[0]=' '
  for i in range(1,9):
    tabuleiro[i]='X'
    aux=[]
    for no in arvore:
      print no
      if not simetrico(no, tabuleiro):
        aux+=[copiar(tabuleiro)]
    tabuleiro[i]=' '
    arvore+=aux
  return arvore

gerarArvore()