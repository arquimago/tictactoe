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

def copia(tab):
  tabuleiro=[]
  for celula in tab:
    tabuleiro+=celula
  return tabuleiro

def rodar(tab):
  tabuleiro=[]
  tabuleiro+=tab[3]
  tabuleiro+=tab[6]
  tabuleiro+=tab[9]
  tabuleiro+=tab[2]
  tabuleiro+=tab[5]
  tabuleiro+=tab[8]
  tabuleiro+=tab[1]
  tabuleiro+=tab[4]
  tabuleiro+=tab[7]
  return tabuleiro

def espelhar(tab):
  tabuleiro=[]
  tabuleiro+=tab[3]
  tabuleiro+=tab[2]
  tabuleiro+=tab[1]
  tabuleiro+=tab[6]
  tabuleiro+=tab[5]
  tabuleiro+=tab[4]
  tabuleiro+=tab[9]
  tabuleiro+=tab[8]
  tabuleiro+=tab[7]
  return tabuleiro  

def igual(tab1,tab2):
  for i in range(0,9):
    if tab1[i]!=tab2[i]:
	  return False
  return True

def simetrico(tab1,tab2):
  tabTemp = tab2
  for i in range(0,4):
    if igual(tab1,tabTemp):
	  return True
	tabTemp = espelhar(tabTemp)
	if igual(tab1,tabTemp):
	  return True
	tabTemp = espelhar(tabTemp)
	tabTemp = rodar(tabTemp)
  return False

arvore = []
