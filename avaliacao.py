"FUNCAO DE AVALIACAO"
Created on 17/05/2015

@author: Saulo


def avaliacao(state):
    """Retorna o valor da função de avaliação para um determinado nó
    da arvore.
    Esta função recebe uma lista referente ao nó da árvore ou estado atual de uma jogada.
    Por exemplo no nó:
     _O_|_X_|___
     ___|___|___
        |   |
    Lista = ['O','X','','','','','','',''] e retorna o valor -2(para este caso)
        """

    posicao_x = -1
    posicao_o = -1
    x1 = 0
    x2 = 0
    o1 = 0
    o2 = 0
    for indice, valor in enumerate(state):
        if(valor.upper() == 'X'):
            posicao_x = (indice + 1)
        if(valor.upper() == 'O'):
            posicao_o = (indice + 1)

    if(posicao_x == 1):
        x1,x2 = case_1(state,'X')
    elif(posicao_x == 2):
        x1,x2 = case_2(state,'X')
    elif(posicao_x == 3):
        x1,x2 = case_3(state,'X')
    elif(posicao_x == 4):
        x1,x2 = case_4(state,'X')
    elif(posicao_x == 5):
        x1,x2 = case_5(state,'X')
    elif(posicao_x == 6):
        x1,x2 = case_6(state,'X')
    elif(posicao_x == 7):
        x1,x2 = case_7(state,'X')
    elif(posicao_x == 8):
        x1,x2 = case_8(state,'X')
    elif(posicao_x == 9):
        x1,x2 = case_9(state,'X')

    if(posicao_o == 1):
        o1,o2 = case_1(state,'O')
    elif(posicao_o == 2):
        o1,o2 = case_2(state,'O')
    elif(posicao_o == 3):
        o1,o2 = case_3(state,'O')
    elif(posicao_o == 4):
        o1,o2 = case_4(state,'O')
    elif(posicao_o == 5):
        o1,o2 = case_5(state,'O')
    elif(posicao_o == 6):
        o1,o2 = case_6(state,'O')
    elif(posicao_o == 7):
        o1,o2 = case_7(state,'O')
    elif(posicao_o == 8):
        o1,o2 = case_8(state,'O')
    elif(posicao_o == 9):
        o1,o2 = case_9(state,'O')

    return(((6*x2)+(2*x1)) - ((6*o2)+(2*o1)))

def case_1(state,letra):
    x1 = 0
    x2 = 0

    "Linha 1"
    if(state[1] == '' and state[2] == ''):
        x1 += 1
    elif((state[1] == letra and state[2] == '') or
         (state[1] == '' and state[2] == letra)):
        x2 += 1
    "Coluna 1"
    if(state[3] == '' and state[6] == ''):
        x1 += 1
    elif((state[3] == letra and state[6] == '') or
         (state[3] == '' and state[6] == letra)):
        x2 += 1
    "Diagonal 0 -> 8"
    if(state[4] == '' and state[8] == ''):
        x1 += 1
    elif((state[4] == letra and state[8] == '') or
         (state[4] == '' and state[8] == letra)):
        x2 += 1

    return(x1,x2)

def case_2(state,letra):
    x1 = 0
    x2 = 0

    "Linha 1"
    if(state[0] == '' and state[2] == ''):
        x1 += 1
    elif((state[0] == letra and state[2] == '') or
         (state[0] == '' and state[2] == letra)):
        x2 += 1
    "Coluna 2"
    if(state[4] == '' and state[7] == ''):
        x1 += 1
    elif((state[4] == letra and state[7] == '') or
         (state[4] == '' and state[7] == letra)):
        x2 += 1

    return(x1,x2)

def case_3(state,letra):
    x1 = 0
    x2 = 0

    "Linha 1"
    if(state[0] == '' and state[1] == ''):
        x1 += 1
    elif((state[0] == letra and state[1] == '') or
         (state[0] == '' and state[1] == letra)):
        x2 += 1
    "Coluna 3"
    if(state[5] == '' and state[8] == ''):
        x1 += 1
    elif((state[5] == letra and state[8] == '') or
         (state[5] == '' and state[8] == letra)):
        x2 += 1
    "Diagonal 2 -> 6"
    if(state[4] == '' and state[6] == ''):
        x1 += 1
    elif((state[4] == letra and state[6] == '') or
         (state[4] == '' and state[6] == letra)):
        x2 += 1

    return(x1,x2)

def case_4(state,letra):
    x1 = 0
    x2 = 0

    "Linha 2"
    if(state[4] == '' and state[5] == ''):
        x1 += 1
    elif((state[4] == letra and state[5] == '') or
         (state[4] == '' and state[5] == letra)):
        x2 += 1
    "Coluna 1"
    if(state[0] == '' and state[6] == ''):
        x1 += 1
    elif((state[0] == letra and state[6] == '') or
         (state[0] == '' and state[6] == letra)):
        x2 += 1

    return(x1,x2)

def case_5(state,letra):
    x1 = 0
    x2 = 0

    "Linha 2"
    if(state[3] == '' and state[5] == ''):
        x1 += 1
    elif((state[3] == letra and state[5] == '') or
         (state[3] == '' and state[5] == letra)):
        x2 += 1
    "Coluna 2"
    if(state[1] == '' and state[7] == ''):
        x1 += 1
    elif((state[1] == letra and state[7] == '') or
         (state[1] == '' and state[7] == letra)):
        x2 += 1
    "Diagonal 2 -> 6"
    if(state[2] == '' and state[6] == ''):
        x1 += 1
    elif((state[2] == letra and state[6] == '') or
         (state[2] == '' and state[6] == letra)):
        x2 += 1
    "Diagonal 0 -> 8"
    if(state[0] == '' and state[8] == ''):
        x1 += 1
    elif((state[0] == letra and state[8] == '') or
         (state[0] == '' and state[8] == letra)):
        x2 += 1

    return(x1,x2)

def case_6(state,letra):
    x1 = 0
    x2 = 0

    "Linha 2"
    if(state[3] == '' and state[4] == ''):
        x1 += 1
    elif((state[3] == letra and state[4] == '') or
        (state[3] == '' and state[4] == letra)):
        x2 += 1
    "Coluna 3"
    if(state[2] == '' and state[8] == ''):
        x1 += 1
    elif((state[2] == letra and state[8] == '') or
        (state[2] == '' and state[8] == letra)):
        x2 += 1

    return(x1,x2)

def case_7(state,letra):
    x1 = 0
    x2 = 0

    "Linha 3"
    if(state[7] == '' and state[8] == ''):
        x1 += 1
    elif((state[7] == letra and state[8] == '') or
         (state[7] == '' and state[8] == letra)):
        x2 += 1
    "Coluna 1"
    if(state[3] == '' and state[0] == ''):
        x1 += 1
    elif((state[3] == letra and state[0] == '') or
         (state[3] == '' and state[0] == letra)):
        x2 += 1
    "Diagonal 2 -> 6"
    if(state[4] == '' and state[2] == ''):
        x1 += 1
    elif((state[4] == letra and state[2] == '') or
         (state[4] == '' and state[2] == letra)):
        x2 += 1

    return(x1,x2)

def case_8(state,letra):
    x1 = 0
    x2 = 0

    "Linha 3"
    if(state[6] == '' and state[8] == ''):
        x1 += 1
    elif((state[6] == letra and state[8] == '') or
        (state[6] == '' and state[8] == letra)):
        x2 += 1
    "Coluna 2"
    if(state[1] == '' and state[4] == ''):
        x1 += 1
    elif((state[1] == letra and state[4] == '') or
        (state[1] == '' and state[4] == letra)):
        x2 += 1

    return(x1,x2)

def case_9(state,letra):
    x1 = 0
    x2 = 0

    "Linha 3"
    if(state[6] == '' and state[7] == ''):
        x1 += 1
    elif((state[6] == letra and state[7] == '') or
         (state[6] == '' and state[7] == letra)):
        x2 += 1
    "Coluna 3"
    if(state[2] == '' and state[5] == ''):
        x1 += 1
    elif((state[2] == letra and state[5] == '') or
         (state[2] == '' and state[5] == letra)):
        x2 += 1
    "Diagonal 0 -> 8"
    if(state[0] == '' and state[4] == ''):
        x1 += 1
    elif((state[0] == letra and state[4] == '') or
         (state[0] == '' and state[4] == letra)):
        x2 += 1

    return(x1,x2)
