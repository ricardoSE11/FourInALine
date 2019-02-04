import ctypes
import tkinter as tk
from tkinter import *
from tkinter import simpledialog


def prueba():
    print ("Estoy vivo")

testM = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print ("Game console:")


#Global variables.

playerOneName = " "

playerTwoName = " "

playerTurn = 0

gameCompleteBoard = [
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]]

displayedBoard = [
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]]

#Defines the index that will be shown in the board.
currentBoardPosition = 0

#Logic for Main Window

def printBoard(matrix):
    for row in matrix:
        print(row)

#Logic for Player vs Player Window.

def openPlayervsPlayerDataWindow():
    pvpWindowData = Tk()
    print ("Creating a PvP Data window.")
    pvpWindowData.title("Player vs Player")
    pvpWindowData.geometry("600x500+200+100")

    btnPlay = Button(pvpWindowData , text="Play.")
    btnPlay.config(command=openPvPNewBoard)
    btnPlay.place(x=250,y=250)

    mainWindow.destroy()

#FIXME: --- O ---

#Logic for chip moves.
#D:Función que identifica si hay empate. Pero solo se fija en la primera fila (matriz finita)
#E:Un tablero (arreglo)
#S:Valor booleano (True si hay empate, False si no)
#R:Que el tablero sea finito
def empate(tablero):
    for i in range(len(tablero[0])):
        if tablero[0][i] == 0:
            return False

    return True

#D:Función que detecta si hay 4 fichas del mismo tipo seguidas en una fila
#E:Un arreglo y dós números (tablero , i , j)
#S:Valor booleano (True si gano, False si no)
#R:Ninguna*
def chequear_fila(t,i,j):
    if t[i][j] == t[i][j+1] == t[i][j+2] == t[i][j+3]!= 0:
        return True


#D:Función que detecta si hay 4 fichas del mismo tipo seguidas en una columna
#E:Un arreglo y dós números (tablero , i , j)
#S:Valor booleano (True si ganó, False si no)
#R:Ninguna*
def chequear_columna(t,i,j):
    if t[i][j] == t[i+1][j] == t[i+2][j] == t[i+3][j]!= 0:
        return True


#D:Función que revisa las diagonales Decrecientes en la parte superior del tablero para ver si hay ganador
#E:Un arreglo y dos números (el tablero)
#S:Valor booleano (True si hay ganador, False si no)
#R:Ninguna*
def diagonal_Decreciente_superior(t):
    f = 0
    c = 0
    for i in range (4):
        if t[f][c] == t[f + 1][c + 1] == t[f + 2][c + 2] == t[f + 3][c + 3] != 0:
            return True
        else:
            c += 1

    return False

#D:Función que revisa las diagonales Decrecientes en la parte inferior del tablero para ver si hay ganador
#E:Un arreglo y dos números (el tablero)
#S:Valor booleano (True si hay ganador, False si no)
#R:Ninguna*
def diagonal_Decreciente_inferior(t):
    f = 2
    c = 0
    for i in range (4):
        if t[f][c] == t[f + 1][c + 1] == t[f + 2][c + 2] == t[f + 3][c + 3] != 0:
            return True
        else:
            c += 1

    return False

#D:Función que revisa las diagonales Crecientes en la parte superior del tablero para ver si hay ganador
#E:Un arreglo y dos números (el tablero)
#S:Valor booleano (True si hay ganador, False si no)
#R:Ninguna*
def diagonal_Creciente_superior(t):
    f = 3 #f de fila
    c = 0 #c de columna
    for i in range(4):
        if t[f][c] == t[f - 1][c + 1] == t[f - 2][c + 2] == t[f - 3][c + 3] != 0:
            return True
        else:
            c += 1

    return False

#D:Función que revisa las diagonales Crecientes en la parte inferior del tablero para ver si hay ganador
#E:Un arreglo y dos números (el tablero)
#S:Valor booleano (True si hay ganador, False si no)
#R:Ninguna*
def diagonal_Creciente_inferior(t):
    f = 5 #f de fila
    c = 0 #c de columna
    for i in range(4):
        if t[f][c] == t[f - 1][c + 1] == t[f - 2][c + 2] == t[f - 3][c + 3] != 0:
            return True
        else:
            c += 1

    return False


#D:Función que revisa las líneas del centro para ver si hay un ganador
#E:Un arreglo (el tablero)
#S:Un valor booleano (True si hay ganador, False si no)
#R:Ninguna*
def diagonal_centro_decreciente(t):
    if t[1][1] == t[2][2] == t[3][3] == t[4][4] != 0:
        return True
    if t[1][2] == t[2][3] == t[3][4] == t[4][5] != 0:
        return True
    if t[0][0] == t[1][1] == t[2][2] == t[3][3] != 0:
        return True
    if t[1][0] == t[2][1] == t[3][2] == t[4][3] != 0:
        return True
    if t[0][1] == t[1][2] == t[2][3] == t[3][4] != 0:
        return True
    if t[1][3] == t[2][4] == t[3][5] == t[4][6] != 0:
        return True

    else:
        return False

#D:Función que revisa las líneas del centro para ver si hay un ganador
#E:Un arreglo (el tablero)
#S:Un valor booleano (True si hay ganador, False si no)
#R:Ninguna*
def diagonal_centro_creciente(t):
    if t[4][0] == t[3][1] == t[2][2] == t[1][3] != 0:
        return True
    if t[4][1] == t[3][2] == t[2][3] == t[1][4] != 0:
        return True
    if t[4][2] == t[3][3] == t[2][4] == t[1][5] != 0:
        return True

    if t[4][3] == t[3][4] == t[2][5] == t[1][6] != 0:
        return True
    else:
        return False


#D:Función para saber si hay ganador
#E:Un arreglo (tablero)
#S:Valor booleano (True si hay ganador, False si no)
#R:Ninguna*
def hayGanador(tablero, N, M):
    for i in range(N):
        for j in range (M):
            if  (j + 3) < M and chequear_fila(tablero,i,j):
                return True
            if (i + 3) < N and chequear_columna(tablero ,i,j):
                return True
    if diagonal_Decreciente_superior(tablero):
        return True

    if diagonal_Decreciente_inferior(tablero):
        return True

    if diagonal_centro_decreciente(tablero):
        return True

    #if diagonal_centro_creciente(tablero):
        #return True

    if diagonal_Creciente_superior(tablero):
        return True

    if diagonal_Creciente_inferior(tablero):
        return True



    else:
        return False

#FIXME: --- O ---

def isColumnEmpty(matrix, column):
    for i in range(len(matrix)):
        if matrix[i][column] != 0:
            return False

        return True

def isColumnFull(matrix,column):
    for i in range(len(matrix)):
        if matrix[i][column] == 0:
            return False

        return True

def getNextPosition(matrix, column):
    rows = len(matrix) - 1
    for i in range(len(matrix)) : #For each row.
        if (matrix[rows][column]) == 0:
            #print (rows)
            return rows #Note: Returns the position of an empty space.

        else:
            rows = rows - 1

    return -1

def placeChip(row,column):
    global  gameCompleteBoard
    global playerTurn

    print ("Clicked button: " ,row , " " , column)

    if (isColumnFull(gameCompleteBoard,column)):
        ctypes.windll.user32.MessageBoxW(0, "Ya no hay más espacio en esta columna, pendejo.", "Bato ciego.", 1)

    position = getNextPosition(gameCompleteBoard,column)
    print("Attempt to play in position: ", position, " " ,column)
    if (playerTurn%2 == 0):
        gameCompleteBoard[position][column] = "2"
        exec ("button{}{}.config(image = yellowDot)".format(position,column))
        playerTurn = playerTurn + 1
        printBoard(gameCompleteBoard)
        if (hayGanador(gameCompleteBoard,6,7)):
            simpledialog.messagebox._show("GANADOR","GANÓ EL AMARILLO",None,None)

    else:
        gameCompleteBoard[position][column] = "1"
        exec ("button{}{}.config(image = redDot)".format(position,column))
        playerTurn = playerTurn + 1
        printBoard(gameCompleteBoard)
        if (hayGanador(gameCompleteBoard,6,7)):
            simpledialog.messagebox._show("GANADOR","GANÓ EL ROJO",None,None)



def openPvPNewBoard():
    global emptySpace
    global yellowDot
    global redDot

    global playerTurn
    global playerOneName
    global playerTwoName
    print ("Creating a new game board for players: " , playerOneName , "and " , playerTwoName)

    pvpWindow = Tk()
    pvpWindow.title("Bato 1 vs Bato 2")
    pvpWindow.geometry("900x900+400+40")
    pvpWindow.maxsize(width=900, height=900)

    #Images for buttons to increase the size of the board.
    upArrow = PhotoImage(file = "up-arrow.png")
    rightArrow = PhotoImage(file = "right-arrow.png")
    leftArrow = PhotoImage(file = "left-arrow.png")
    downArrow = PhotoImage(file = "down-arrow.png")

    #Buttons to increase the size of the board.
    btnAddRow = Button(pvpWindow , image=upArrow , width=735, bg="darkred") #TODO: Add command to the buttons
    btnAddRow.image=upArrow
    btnAddRow.place(x=95,y=143)
    btnAddRow.config(command= lambda:addRowToMatrix(gameCompleteBoard))

    btnAddRightColumn = Button(pvpWindow , image=rightArrow ,height=640, bg="darkred")
    btnAddRightColumn.image=rightArrow
    btnAddRightColumn.place(x=839,y=165)
    btnAddRightColumn.config(command=lambda:addRowToMatrix(gameCompleteBoard))

    btnAddLeftColumn = Button(pvpWindow , image=leftArrow , height=640, bg="darkred")
    btnAddLeftColumn.image=leftArrow
    btnAddLeftColumn.place(x=72,y=165)

    btnMoveDownOneColumn = Button(pvpWindow , image=downArrow, width=735, bg="darkred")
    btnMoveDownOneColumn.image=downArrow
    btnMoveDownOneColumn.place(x=95,y=815)

    #FIXME

    gameCanvas = Canvas(pvpWindow , width=600 , height=500, bg="blue")
    gameCanvas.place(x=95,y=165)


    #Adds a row to the first position of the list
    def addRowToMatrix(matrix):
        print("--- LOG: Adding a new row to the matrix. ---")
        newRow = [0,0,0,0,0,0,0]
        matrix.insert(0,newRow)

        buttonPrueba = Button(gameCanvas,image=redDot, bg="darkblue",command=lambda:placeChip(1,0))
        buttonPrueba.image=redDot
        buttonPrueba.place(x=0,y=-105)

        printBoard(matrix)
        return matrix

    def addRigthColumnToMatrix(matrix):
        print("--- LOG: Adding a new Right column to the matrix. ---")
        for row in matrix:
            row = row.append(0)

        #buttonRight = Button(gameCanvas,image=redDot, bg="darkblue",command=lambda:placeChip(1,7))
        #buttonRight.image=redDot
        #buttonRight.grid(row=0,column=6)

        printBoard(matrix)

    def addLeftColumnToMatrix(matrix):
        print("--- LOG: Adding a new Left column to the matrix. ---")
        for row in matrix:
            row = row.insert(0,0)


        printBoard(matrix)

    #Images
    emptySpace = PhotoImage(file = "emptyspace.png")
    yellowDot = PhotoImage(file = "yellowDot.png")
    redDot = PhotoImage(file = "redDot.png")

    #Board initial buttons (Empty spaces)
    #NOTE: [1]

    global button00, button01, button02, button03, button04, button05, button06, button10, button11, button12, button13, button14, button15, button16, button20, button21, button22, button23, button24, button25, button26, button30, button31, button32, button33, button34, button35, button36, button40, button41, button42, button43, button44, button45, button46, button50, button51, button52, button53, button53, button54, button55, button56
    button50 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button50.image=emptySpace #Importante para que se vea la imagen
    button50.grid(row=5, column=0)
    button50.config(command=lambda: placeChip(5, 0))

    button40 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button40.image=emptySpace
    button40.grid(row=4, column=0)
    button40.config(command=lambda: placeChip(4, 0))

    button30 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button30.image=emptySpace #Importante para que se vea la imagen
    button30.grid(row=3, column=0)
    button30.config(command=lambda: placeChip(3, 0))

    button20 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button20.image=emptySpace
    button20.grid(row=2, column=0)
    button20.config(command=lambda: placeChip(2, 0))

    button10 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button10.image=emptySpace #Importante para que se vea la imagen
    button10.grid(row=1, column=0)
    button10.config(command=lambda: placeChip(1, 0))

    button00 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button00.image=emptySpace
    button00.grid(row=0, column=0)
    button00.config(command=lambda: placeChip(0, 0))

    #TODO: [2] TODO used to highlight this comment and be able to identify easier de division 2

    button51 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button51.image=emptySpace #Importante para que se vea la imagen
    button51.grid(row=5, column=1)
    button51.config(command=lambda: placeChip(5, 1))

    button41 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button41.image=emptySpace
    button41.grid(row=4, column=1)
    button41.config(command=lambda: placeChip(4, 1))

    button31 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button31.image=emptySpace #Importante para que se vea la imagen
    button31.grid(row=3, column=1)
    button31.config(command=lambda: placeChip(3, 1))

    button21 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button21.image=emptySpace
    button21.grid(row=2, column=1)
    button21.config(command=lambda: placeChip(2, 1))

    button11 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button11.image=emptySpace #Importante para que se vea la imagen
    button11.grid(row=1, column=1)
    button11.config(command=lambda: placeChip(1, 1))

    button01 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button01.image=emptySpace
    button01.grid(row=0, column=1)
    button01.config(command=lambda: placeChip(0, 1))

    #TODO: [3] TODO used to highlight this comment and be able to identify easier de division

    button52 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button52.image=emptySpace #Importante para que se vea la imagen
    button52.grid(row=5, column=2)
    button52.config(command=lambda: placeChip(5, 2))

    button42 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button42.image=emptySpace
    button42.grid(row=4, column=2)
    button42.config(command=lambda: placeChip(4, 2))

    button32 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button32.image=emptySpace #Importante para que se vea la imagen
    button32.grid(row=3, column=2)
    button32.config(command=lambda: placeChip(3, 2))

    button22 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button22.image=emptySpace
    button22.grid(row=2, column=2)
    button22.config(command=lambda: placeChip(2, 2))

    button12 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button12.image=emptySpace #Importante para que se vea la imagen
    button12.grid(row=1, column=2)
    button12.config(command=lambda: placeChip(1, 2))

    button02 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button02.image=emptySpace
    button02.grid(row=0, column=2)
    button02.config(command=lambda: placeChip(0, 2))

    #NOTE: [4] & {3}

    button53 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button53.image=emptySpace #Importante para que se vea la imagen
    button53.grid(row=5, column=3)
    button53.config(command=lambda: placeChip(5, 3))

    button43 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button43.image=emptySpace
    button43.grid(row=4, column=3)
    button43.config(command=lambda: placeChip(4, 3))

    button33 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button33.image=emptySpace #Importante para que se vea la imagen
    button33.grid(row=3, column=3)
    button33.config(command=lambda: placeChip(3, 3))

    button23 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button23.image=emptySpace
    button23.grid(row=2, column=3)
    button23.config(command=lambda: placeChip(2, 3))

    button13 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button13.image=emptySpace #Importante para que se vea la imagen
    button13.grid(row=1, column=3)
    button13.config(command=lambda: placeChip(1, 3))

    button03 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button03.image=emptySpace
    button03.grid(row=0, column=3)
    button03.config(command=lambda: placeChip(0, 3))

    #NOTE: [5] & {4}

    button54 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button54.image=emptySpace #Importante para que se vea la imagen
    button54.grid(row=5, column=4)
    button54.config(command=lambda: placeChip(5, 4))

    button44 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button44.image=emptySpace
    button44.grid(row=4, column=4)
    button44.config(command=lambda: placeChip(4, 4))

    button34 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button34.image=emptySpace #Importante para que se vea la imagen
    button34.grid(row=3, column=4)
    button34.config(command=lambda: placeChip(3, 4))

    button24 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button24.image=emptySpace
    button24.grid(row=2, column=4)
    button24.config(command=lambda: placeChip(2, 4))

    button14 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button14.image=emptySpace #Importante para que se vea la imagen
    button14.grid(row=1, column=4)
    button14.config(command=lambda: placeChip(1, 4))

    button04 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button04.image=emptySpace
    button04.grid(row=0, column=4)
    button04.config(command=lambda: placeChip(0, 4))

    #NOTE: [6] & {5}

    button55 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button55.image=emptySpace #Importante para que se vea la imagen
    button55.grid(row=5, column=5)
    button55.config(command=lambda: placeChip(5, 5))

    button45 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button45.image=emptySpace
    button45.grid(row=4, column=5)
    button45.config(command=lambda: placeChip(4, 5))

    button35 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button35.image=emptySpace #Importante para que se vea la imagen
    button35.grid(row=3, column=5)
    button35.config(command=lambda: placeChip(3, 5))

    button25 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button25.image=emptySpace
    button25.grid(row=2, column=5)
    button25.config(command=lambda: placeChip(2, 5))

    button15 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button15.image=emptySpace #Importante para que se vea la imagen
    button15.grid(row=1, column=5)
    button15.config(command=lambda: placeChip(1, 5))

    button05 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button05.image=emptySpace
    button05.grid(row=0, column=5)
    button05.config(command=lambda: placeChip(0, 5))

    #NOTE: [6] & {5}

    button56 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button56.image=emptySpace #Importante para que se vea la imagen
    button56.grid(row=5, column=6)
    button56.config(command=lambda: placeChip(5, 6))

    button46 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button46.image=emptySpace
    button46.grid(row=4, column=6)
    button46.config(command=lambda: placeChip(4, 6))

    button36 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button36.image=emptySpace #Importante para que se vea la imagen
    button36.grid(row=3, column=6)
    button36.config(command=lambda: placeChip(3, 6))

    button26 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button26.image=emptySpace
    button26.grid(row=2, column=5 + 1)
    button26.config(command=lambda: placeChip(2, 6))

    button16 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button16.image=emptySpace #Importante para que se vea la imagen
    button16.grid(row=1, column=6)
    button16.config(command=lambda: placeChip(1, 6))

    button06 = Button(gameCanvas, image=emptySpace, bg="darkblue")
    button06.image=emptySpace
    button06.grid(row=0, column=6)
    button06.config(command=lambda: placeChip(0, 6))




#GUI
mainWindow = Tk()
mainWindow.title("Four in a line")
mainWindow.geometry("545x545+500+100") #size, position
mainWindow.config(bg="white")
mainWindow.maxsize(width=1170, height=545)


#Buttons
btnPlayerVsPlayer = Button(mainWindow , text = "Player vs Player")
btnPlayerVsPlayer.config(height=3 , width=0)
btnPlayerVsPlayer.config(command=openPlayervsPlayerDataWindow)
btnPlayerVsPlayer.place(x=250,y=200)

btnPlayerVsAi = Button(mainWindow , text = "Player vs AI")
btnPlayerVsAi.config(height=3 , width=0)
btnPlayerVsAi.config(command=lambda:printBoard(gameCompleteBoard))
btnPlayerVsAi.place(x=250,y=300)

btncheckPlayerScores = Button(mainWindow , text = "Scores")
btncheckPlayerScores.config(height=3 , width=0)
btncheckPlayerScores.config(command=lambda:printBoard(gameCompleteBoard))
btncheckPlayerScores.place(x=250,y=400)


mainWindow.mainloop()
