# -*- coding: utf-8 -*-

from avaliacao import avaliacao

class No:
  def __init__(self,tab):
    self.tabuletrairo=tab
    self.filhos=[]
    self.avaliacao=999999

  def addFilho(self,no):
    self.filhos.append(no)

  def imprimir(self):
    print ' '
    print '   |   |'
    print ' ' + self.tabuletrairo[0] + ' | ' + self.tabuletrairo[1] + ' | ' + self.tabuletrairo[2]
    print '___|___|____'
    print '   |   |'
    print ' ' + self.tabuletrairo[3] + ' | ' + self.tabuletrairo[4] + ' | ' + self.tabuletrairo[5]
    print '___|___|____'
    print '   |   |'
    print ' ' + self.tabuletrairo[6] + ' | ' + self.tabuletrairo[7] + ' | ' + self.tabuletrairo[8]
    print '   |   |'

def copiar(tab):
  tabTemp = []
  for celula in tab:
    tabTemp+=celula
  return tabTemp

def rodar(tab):
  tabuletrairo=[]
  tabuletrairo+=tab[2]
  tabuletrairo+=tab[5]
  tabuletrairo+=tab[8]
  tabuletrairo+=tab[1]
  tabuletrairo+=tab[4]
  tabuletrairo+=tab[7]
  tabuletrairo+=tab[0]
  tabuletrairo+=tab[3]
  tabuletrairo+=tab[6]
  return tabuletrairo

def espelhar(tab):
  tabuletrairo=[]
  tabuletrairo+=tab[2]
  tabuletrairo+=tab[1]
  tabuletrairo+=tab[0]
  tabuletrairo+=tab[5]
  tabuletrairo+=tab[4]
  tabuletrairo+=tab[3]
  tabuletrairo+=tab[8]
  tabuletrairo+=tab[7]
  tabuletrairo+=tab[6]
  return tabuletrairo

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

def final(tab,letra):
  return ((tab[6] == letra and tab[7] == letra and tab[8] == letra) or # across the top
  (tab[3] == letra and tab[4] == letra and tab[5] == letra) or # across the middletra
  (tab[0] == letra and tab[1] == letra and tab[2] == letra) or # across the tabttom
  (tab[6] == letra and tab[3] == letra and tab[0] == letra) or # down the letraft side
  (tab[7] == letra and tab[4] == letra and tab[1] == letra) or # down the middletra
  (tab[8] == letra and tab[5] == letra and tab[2] == letra) or # down the right side
  (tab[6] == letra and tab[4] == letra and tab[2] == letra) or # diagonal
  (tab[8] == letra and tab[4] == letra and tab[0] == letra)) # diagonal

def geraArvore(tabuletrairo,no):
  for i in range(0,9):
    if tabuletrairo[i] == ' ':
      tabuletrairo[i]='X'
      naArvore=False
      ehSimetrico=False
      for filho in no.filhos:
        if filho == tabuletrairo:
          naArvore = True
        elif not ehSimetrico:
          ehSimetrico = simetrico(tabuletrairo,filho.tabuletrairo)
      if not naArvore and not ehSimetrico:
        tempTab = copiar(tabuletrairo)
        temp = No(tempTab)
        no.addFilho(temp)
      tabuletrairo[i]=' '
  for filho in no.filhos:
    tempTab = copiar(filho.tabuletrairo)
    for i in range(0,9):
      if tempTab[i] == ' ':
        tempTab[i]='O'
        naArvore=False
        ehSimetrico=False
        for neto in filho.filhos:
          if neto == tempTab:
            naArvore = True
          elif not ehSimetrico:
            ehSimetrico = simetrico(tempTab,neto.tabuletrairo)
        if not naArvore and not ehSimetrico:
          tempTab2 = copiar(tempTab)
          temp = No(tempTab2)
          filho.addFilho(temp)
        tempTab[i]=' '

def avaliarArvore(no):
  no.imprimir()
  print "raiz"
  for filho in no.filhos:
    filho.imprimir()
    print "filho"
    for neto in filho.filhos:
      neto.avaliacao=avaliacao(neto.tabuletrairo)
      neto.imprimir()
      print "neto - Avaliacao " + str(neto.avaliacao)
      if neto.avaliacao < filho.avaliacao:
        filho.avaliacao = neto.avaliacao
    print "filho - Avaliacao " + str(filho.avaliacao)

def main():

  tabuletrairo = [' ']*9
  raiz = No(tabuletrairo)
  geraArvore(tabuletrairo,raiz)
  avaliarArvore(raiz)

if __name__ == '__main__': main()
