# -*- coding: utf-8 -*-

from avaliacao import avaliacao

class No:
  def __init__(self,tab):
    self.tabuleiro=tab
    self.filhos=[]
    self.avaliacao=999999

  def addFilho(self,no):
    self.filhos.append(no)

  def imprimir(self):
    print ' '
    print '   |   |'
    print ' ' + self.tabuleiro[0] + ' | ' + self.tabuleiro[1] + ' | ' + self.tabuleiro[2]
    print '___|___|____'
    print '   |   |'
    print ' ' + self.tabuleiro[3] + ' | ' + self.tabuleiro[4] + ' | ' + self.tabuleiro[5]
    print '___|___|____'
    print '   |   |'
    print ' ' + self.tabuleiro[6] + ' | ' + self.tabuleiro[7] + ' | ' + self.tabuleiro[8]
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

def final(tab,letra):
  return ((tab[6] == letra and tab[7] == letra and tab[8] == letra) or
  (tab[3] == letra and tab[4] == letra and tab[5] == letra) or
  (tab[0] == letra and tab[1] == letra and tab[2] == letra) or
  (tab[6] == letra and tab[3] == letra and tab[0] == letra) or
  (tab[7] == letra and tab[4] == letra and tab[1] == letra) or
  (tab[8] == letra and tab[5] == letra and tab[2] == letra) or
  (tab[6] == letra and tab[4] == letra and tab[2] == letra) or
  (tab[8] == letra and tab[4] == letra and tab[0] == letra))

def geraArvore(tabuleiro,no):
  for i in range(0,9):
    if tabuleiro[i] == ' ':
      tabuleiro[i]='X'
      naArvore=False
      ehSimetrico=False
      for filho in no.filhos:
        if filho == tabuleiro:
          naArvore = True
        elif not ehSimetrico:
          ehSimetrico = simetrico(tabuleiro,filho.tabuleiro)
      if not naArvore and not ehSimetrico:
        tempTab = copiar(tabuleiro)
        temp = No(tempTab)
        no.addFilho(temp)
      tabuleiro[i]=' '
  for filho in no.filhos:
    tempTab = copiar(filho.tabuleiro)
    for i in range(0,9):
      if tempTab[i] == ' ':
        tempTab[i]='O'
        naArvore=False
        ehSimetrico=False
        for neto in filho.filhos:
          if neto == tempTab:
            naArvore = True
          elif not ehSimetrico:
            ehSimetrico = simetrico(tempTab,neto.tabuleiro)
        if not naArvore and not ehSimetrico:
          tempTab2 = copiar(tempTab)
          temp = No(tempTab2)
          filho.addFilho(temp)
        tempTab[i]=' '

def avaliarArvore(no):
  for filho in no.filhos:
    for neto in filho.filhos:
      neto.avaliacao=avaliacao(neto.tabuleiro)
      neto.imprimir()
      print "folha - Avaliacao " + str(neto.avaliacao)


def imprimirArvore(no):
  no.imprimir()
  print "raiz"
  for filho in no.filhos:
    filho.imprimir()
    print "filho"
    for neto in filho.filhos:
      neto.avaliacao=avaliacao(neto.tabuleiro)
      neto.imprimir()
      print "neto"

def main():

  tabuleiro = [' ']*9
  raiz = No(tabuleiro)
  geraArvore(tabuleiro,raiz)
  avaliarArvore(raiz)

if __name__ == '__main__': main()
