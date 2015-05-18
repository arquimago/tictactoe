# -*- coding: utf-8 -*-

class No:
  def __init__(self,tab):
    self.tabuleiro=tab
    self.filhos=[]

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

"""
#a função abaixo gera 1 nivel de arvore
def gerarArvore():
  tabuleiro = [' ']*9
  arvore=[]
  arvore+=[[-1,copiar(tabuleiro)]]
  tabuleiro[0]='X'
  arvore+=[[0,copiar(tabuleiro)]]
  tabuleiro[0]=' '
  for i in range(1,9):
    tabuleiro[i]='X'
    naArvore = False
    ehSimetrico = False
    for no in arvore:
      if no[1] == tabuleiro:
        naArvore = True
      elif not ehSimetrico:
        ehSimetrico = simetrico(tabuleiro,no[1])
    if not naArvore and not ehSimetrico:
      arvore+=[[0,copiar(tabuleiro)]]
    tabuleiro[i]=' '
  return arvore
"""

def geraArvore(tabuleiro,no,nivel,letra):
  if nivel == 2:
    return
  for i in range(0,9):
    print nivel
    if tabuleiro[i] == ' ':
      tabuleiro[i]=letra
      print tabuleiro
      naArvore=False
      ehSimetrico=False
      for filho in no.filhos:
        if filho == tabuleiro:
          naArvore = True
        elif not ehSimetrico:
          ehSimetrico = simetrico(tabuleiro,filho.tabuleiro)
      if not naArvore and not ehSimetrico:
        temp = No(tabuleiro)
        no.addFilho(temp)
        if letra == 'X':
          letra = 'O'
        else:
          letra = 'X'
        geraArvore(tabuleiro,no.filhos[len(no.filhos)-1],nivel+1,letra)
    tabuleiro[i]=' '

#print gerarArvore()

tabuleiro = [' ']*9
raiz = No(tabuleiro)

geraArvore(tabuleiro,raiz,0,'X')
