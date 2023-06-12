import random

class TicTacToe:
    def __init__(self):
        self.contadorMovimientos = 0
        self.palabras = ""

        self.fichas = [" ", " "]

        self.matrizTablero = [[" ", " ", " "],
                              [" ", " ", " "],
                              [" ", " ", " "]]

    def jugar(self):
        self.seleccionarFicha()
        self.tablero()
        self.turnos()

    def seleccionarFicha(self):
        ficha = (input("Seleccione ficha X / O:\n")).upper()
        if(ficha == "X"):
            self.fichas[0] = "X"
            self.fichas[1] = "O"
        elif(ficha == "O"):
            self.fichas[0] = "O"
            self.fichas[1] = "X"
        else:
            print("Por favor, seleccione una ficha valida\n")
            self.seleccionarFicha()

    def turnos(self):
        if(self.fichas[0] == "X"):
            self.movimientoJugador1()
        else:
            self.movimientoJugador2()

    def movimientoJugador1(self):
        casillas = int(input(F"Seleccione casilla jugador {self.fichas[0]}: "))
        filas = int((casillas - 1)/3)
        columnas = (casillas - 3*(int((casillas - 1)/3))) - 1

        if( (casillas > 0) and (casillas <10) ):
            if( (self.matrizTablero[filas][columnas]) == " "):
                self.contadorMovimientos += 1
                self.matrizTablero[filas][columnas] = self.fichas[0]
                self.tablero()
                self.palabras = self.ganador(self.fichas[0], self.contadorMovimientos)

                if(self.palabras != " "):
                    print(self.palabras)
                else:
                    self.movimientoJugador2()

            elif( (self.matrizTablero[filas][columnas] == self.fichas[0]) or (self.matrizTablero[filas][columnas] == self.fichas[1]) ):
                print("Casilla no disponible, por favor seleccione otra\n")
                self.movimientoJugador1()
        else:
            print("Por favor, seleccione una casilla valida\n")
            self.movimientoJugador1()

    def movimientoJugador2(self):
        casillas = int(input(F"Seleccione casilla jugador {self.fichas[1]}: "))
        filas = int((casillas - 1)/3)
        columnas = (casillas - 3*(int((casillas - 1)/3))) - 1

        if( (casillas > 0) and (casillas <10) ):
            if( (self.matrizTablero[filas][columnas]) == " "):
                self.contadorMovimientos += 1
                self.matrizTablero[filas][columnas] = self.fichas[1]
                self.tablero()
                self.palabras = self.ganador(self.fichas[1], self.contadorMovimientos)

                if(self.palabras != " "):
                    print(self.palabras)
                else:
                    self.movimientoJugador1()

            elif( (self.matrizTablero[filas][columnas] == self.fichas[0]) or (self.matrizTablero[filas][columnas] == self.fichas[1]) ):
                print("Casilla no disponible, por favor seleccione otra\n")
                self.movimientoJugador2()
        else:
            print("Por favor, seleccione una casilla valida\n")
            self.movimientoJugador2()

    def ganador(self, fichaTurno, numeroMovimiento):
        if(numeroMovimiento == 9):
            return "Juego empatado"
        else:
            return self.revisarFilas(fichaTurno)

    def revisarFilas(self, jugador):
        for i in range(0, 3):
            if(self.matrizTablero[i][0] == self.matrizTablero[i][1] == self.matrizTablero[i][2] == jugador):
                return F"Juego ganado por {jugador}"

        return self.revisarColumnas(jugador)

    def revisarColumnas(self, jugador):
        for i in range(0, 3):
            if(self.matrizTablero[0][i] == self.matrizTablero[1][i] == self.matrizTablero[2][i] == jugador):
                return F"Juego ganado por {jugador}"

        return self.revisarDiagonales(jugador)

    def revisarDiagonales(self, jugador):
        if(self.matrizTablero[0][0] == self.matrizTablero[1][1] == self.matrizTablero[2][2] == jugador):
            return F"Juego ganado por {jugador}"
        elif(self.matrizTablero[2][0] == self.matrizTablero[1][1] == self.matrizTablero[0][2] == jugador):
            return F"Juego ganado por {jugador}"
        else:
            return " "


    def tablero(self):
        print("\n")
        print("            |            |         ")
        print(f"1     {self.matrizTablero[0][0]}     |2     {self.matrizTablero[0][1]}     |3     {self.matrizTablero[0][2]}     ")
        print("            |            |         ")
        print("---------------------------------------")
        print("            |            |         ")
        print(f"4     {self.matrizTablero[1][0]}     |5     {self.matrizTablero[1][1]}     |6     {self.matrizTablero[1][2]}     ")
        print("            |            |         ")
        print("---------------------------------------")
        print("            |            |         ")
        print(f"7     {self.matrizTablero[2][0]}     |8     {self.matrizTablero[2][1]}     |9     {self.matrizTablero[2][2]}     ")
        print("            |            |         ")
        print("\n")
        print("\n")

TicTacToe().jugar()
