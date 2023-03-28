#Tic-Tac-Toe Game

from re import X


Board = {"1":" ","2":" ","3":" ",
       "4":" ","5":" ","6":" ",
       "7":" ","8":" ","9":" "}

availableMove = {"1":"1","2":"2","3":"3",
       "4":"4","5":"5","6":"6",
       "7":"7","8":"8","9":"9"}

def printInfo():
    print("")
    print(availableMove["1"]+"|"+availableMove["2"]+"|"+availableMove["3"]+"              "+Board["1"]+"|"+Board["2"]+"|"+Board["3"])
    print("-+-+-"+"              "+"-+-+-")   
    print(availableMove["4"]+"|"+availableMove["5"]+"|"+availableMove["6"]+"              "+Board["4"]+"|"+Board["5"]+"|"+Board["6"])
    print("-+-+-"+"              "+"-+-+-")    
    print(availableMove["7"]+"|"+availableMove["8"]+"|"+availableMove["9"]+"              "+Board["7"]+"|"+Board["8"]+"|"+Board["9"])
    print("")

def clearGame():

    Board = {"1":" ","2":" ","3":" ",
       "4":" ","5":" ","6":" ",
       "7":" ","8":" ","9":" "}

    availableMove = {"1":"1","2":"2","3":"3",
       "4":"4","5":"5","6":"6",
       "7":"7","8":"8","9":"9"}


def playerOne():
    while True:
        printInfo()
        move  = str(input("Jugador 1, seleccione el lugar en el que desea realizar la jugada: "))
        if(move not in availableMove.keys() or Board[move] == "X" or Board[move] == "O"):
            print("")
            print("Ingrese una opción válida!")
            continue
        else:
            availableMove[move] = " "
            Board[move] = "X"
            break



def playerTwo():
    while True:
        printInfo()
        move  = str(input("Jugador 2, seleccione el lugar en el que desea realizar la jugada: "))
        if(move not in availableMove.keys() or Board[move] == "X" or Board[move] == "O"):
            print("")
            print("Ingrese una opción válida!")
            continue
        else:
            availableMove[move] = " "
            Board[move] = "O"
            break

def ganador():
    #Bloque de posibilidades para ganador 1:
    if(Board["1"] == "X" and Board["2"] == "X" and Board["3"] == "X"):
        printInfo()
        print("El ganador es el jugador 1, felicitaciones!")
        exit()
    elif(Board["4"] == "X" and Board["5"] == "X" and Board["6"] == "X"):
        printInfo()
        print("El ganador es el jugador 1, felicitaciones!")
        exit()
    elif(Board["7"] == "X" and Board["8"] == "X" and Board["9"] == "X"):
        printInfo()
        print("El ganador es el jugador 1, felicitaciones!")
        exit()
    elif(Board["1"] == "X" and Board["4"] == "X" and Board["7"] == "X"):
        printInfo()
        print("El ganador es el jugador 1, felicitaciones!")
        exit()
    elif(Board["2"] == "X" and Board["5"] == "X" and Board["8"] == "X"):
        printInfo()
        print("El ganador es el jugador 1, felicitaciones!")
        exit()
    elif(Board["3"] == "X" and Board["6"] == "X" and Board["9"] == "X"):
        printInfo()
        print("El ganador es el jugador 1, felicitaciones!")
        exit()
    elif(Board["1"] == "X" and Board["5"] == "X" and Board["9"] == "X"):
        printInfo()
        print("El ganador es el jugador 1, felicitaciones!")
        exit()
    elif(Board["3"] == "X" and Board["5"] == "X" and Board["7"] == "X"):
        printInfo()
        print("El ganador es el jugador 1, felicitaciones!")
        exit()
    
    #Bloque de posibilidades para ganador 2:
    elif(Board["1"] == "O" and Board["2"] == "O" and Board["3"] == "O"):
        printInfo()
        print("El ganador es el jugador 1, felicitaciones!")
        exit()
    elif(Board["4"] == "O" and Board["5"] == "O" and Board["6"] == "O"):
        printInfo()
        print("El ganador es el jugador 1, felicitaciones!")
        exit()
    elif(Board["7"] == "O" and Board["8"] == "O" and Board["9"] == "O"):
        printInfo()
        print("El ganador es el jugador 1, felicitaciones!")
        exit()
    elif(Board["1"] == "O" and Board["4"] == "O" and Board["7"] == "O"):
        printInfo()
        print("El ganador es el jugador 1, felicitaciones!")
        exit()
    elif(Board["2"] == "O" and Board["5"] == "O" and Board["8"] == "O"):
        printInfo()
        print("El ganador es el jugador 1, felicitaciones!")
        exit()
    elif(Board["3"] == "O" and Board["6"] == "O" and Board["9"] == "O"):
        printInfo()
        print("El ganador es el jugador 1, felicitaciones!")
        exit()
    elif(Board["1"] == "O" and Board["5"] == "O" and Board["9"] == "O"):
        printInfo()
        print("El ganador es el jugador 1, felicitaciones!")
        exit()
    elif(Board["3"] == "O" and Board["5"] == "O" and Board["7"] == "O"):
        printInfo()
        print("El ganador es el jugador 1, felicitaciones!")
        exit()
    

def ticTacToe():
    print("")
    count = 0
    while (count < 10):
        playerOne()
        ganador()
        count += 1
        if(count == 9):
            print("La partida ha finalizado, es un empate!")
            break
        playerTwo()
        ganador()
        count += 1
        


def mainMenu():
    while True:
        print("")
        print(" 1. Instrucciones\n","2. Tic-Tac-Toe\n","3. Salir")
        option = str(input("\nIngrese una opción: "))
        print("")
        if(option == "1"):
            print("Para ingresar al juego, debe seleccionar la opción Tic-Tac-Toe.\nLa pantalla muestra qué jugador debe realizar una jugada. Cada vez que un jugador realiza una jugada, se visualiza el tablero. El juego finaliza cuando se llenen todos los espacios.\n")
        elif(option == "2"):
            ticTacToe()
        elif(option == "3"):
            print("Gracias por usar el juego, feliz día!\n")
            exit()
        else:
            print("Ingrese una opción válida!\n")
            continue
mainMenu()