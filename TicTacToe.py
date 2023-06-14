import random

class TicTacToe:
    def __init__(self):
        self.contadorMovimientos = 0
        self.opciones = ["1 JUGADOR", "2 JUGADORES", "SALIR", "FACIL", "INTERMEDIO", "DIFICIL"]
        self.nivel = 0
        self.modalidad = 0
        self.turno = False

    def jugar(self):
        self.modoDeJuego()
        if(self.opciones[self.modalidad - 1] == "1 JUGADOR"):
            self.seleccionarNivel()
            fichas = self.seleccionarFicha()
            matrizTablero = Tablero().inicializarTablero()
            self.turnos(matrizTablero, fichas)
        elif(self.opciones[self.modalidad - 1] == "2 JUGADORES"):
            fichas = self.seleccionarFicha()
            matrizTablero = Tablero().inicializarTablero()
            self.turnos(matrizTablero, fichas)
        else:
            print("\nJUEGO TERMINADO")

    def modoDeJuego(self):
        seleccion = input(F"Seleccione el siguiente numero para la modalidad:\n1 para {self.opciones[0]} \n2 para {self.opciones[1]} \n3 para {self.opciones[2]}\n\nMODO DE JUEGO: ")
        if(seleccion.isdigit() == True):
            self.modalidad = int(seleccion)
            if( (self.modalidad > 0) and (self.modalidad < 4) ):
                return
            else:
                print("Por favor, seleccione una modalidad valida\n")
                self.modoDeJuego()
        else:
            print("Por favor, seleccione un numero\n")
            self.modoDeJuego()

    def seleccionarNivel(self):
        seleccion = input(F"\nSeleccione el siguiente numero para la dificultad:\n1 para {self.opciones[3]} \n2 para {self.opciones[4]} \n3 para {self.opciones[5]}\n\nDIFICULTAD DE JUEGO: ")
        if(seleccion.isdigit() == True):
            self.nivel = int(seleccion)
            if( (self.nivel > 0) and (self.nivel < 4)):
                return
            else:
                print("Por favor, seleccione un nivel valido\n")
                self.seleccionarNivel()
        else:
            print("Por favor, seleccione un numero\n")
            self.modoDeJuego()

    def seleccionarFicha(self):
        if(self.opciones[self.modalidad - 1] == "1 JUGADOR"):
            aleatorio = random.randint(1, 10)
            if( (aleatorio > 0) and (aleatorio < 5) ):
                fichas = ["X", "O"]
                print("INICIA MAQUINA\n")
                return fichas
            else:
                fichas = ["O", "X"]
                print("INICIA JUGADOR 1\n")
                return fichas
        else:
            ficha = (input("Seleccione ficha X / O:\n")).upper()
            if(ficha == "X"):
                fichas = ["X", "O"]
                print("INICIA JUGADOR 1\n")
                return fichas
            elif(ficha == "O"):
                fichas = ["O", "X"]
                print("INICIA JUGADOR 2\n")
                return fichas
            else:
                print("Por favor, seleccione una ficha valida\n")
                self.seleccionarFicha()

    def turnos(self, matrizTablero, fichas):
        if( (self.opciones[self.modalidad - 1] == "1 JUGADOR") ):
            if(fichas[0] == "X"):
                Maquina(fichas, matrizTablero, self.contadorMovimientos, self.modalidad, self.opciones, self.nivel, self.turno).movimientoJugador()
            else:
                self.turno = int(not self.turno)
                Persona1(fichas, matrizTablero, self.contadorMovimientos, self.modalidad, self.opciones, self.nivel, self.turno).movimientoJugador()
        else:
            if(fichas[0] == "X"):
                Persona1(fichas, matrizTablero, self.contadorMovimientos, self.modalidad, self.opciones, self.nivel, self.turno).movimientoJugador()
            else:
                self.turno = int(not self.turno)
                Persona2(fichas, matrizTablero, self.contadorMovimientos, self.modalidad, self.opciones, self.nivel, self.turno).movimientoJugador()

class Persona1(TicTacToe):
    def __init__(self, fichas, matrizTablero, contadorMovimientos, modalidad, opciones, nivel, turno):
        super().__init__()

        self.palabras = ""

        self.fichas = fichas
        self.matrizTablero = matrizTablero
        self.contadorMovimientos = contadorMovimientos
        self.modalidad = modalidad
        self.opciones = opciones
        self.nivel = nivel
        self.turno = turno

    def movimientoJugador(self):
        seleccion = input(F"Seleccione casilla jugador {self.fichas[self.turno]}: ")
        if(seleccion.isdigit() == True):
            casillas = int(seleccion)
            if( (casillas > 0) and (casillas <10) ):
                filas = int((casillas - 1)/3)
                columnas = (casillas - 3*(int((casillas - 1)/3))) - 1
                if( (self.matrizTablero[filas][columnas]) == " "):
                    self.contadorMovimientos += 1
                    self.matrizTablero[filas][columnas] = self.fichas[self.turno]
                    Tablero().mostrarTablero(self.matrizTablero)
                    self.palabras = Ganador().revisarGanador(self.fichas[self.turno], self.contadorMovimientos, self.matrizTablero)
                    self.turno = int(not self.turno)

                    if(self.palabras != " "):
                        print(self.palabras)
                    else:
                        if( (self.opciones[self.modalidad - 1] == "1 JUGADOR") ):
                            Maquina(self.fichas, self.matrizTablero, self.contadorMovimientos, self.modalidad, self.opciones, self.nivel, self.turno).movimientoJugador()
                        else:
                            Persona2(self.fichas, self.matrizTablero, self.contadorMovimientos, self.modalidad, self.opciones, self.nivel, self.turno).movimientoJugador()

                else:
                    print("Casilla no disponible, por favor seleccione otra\n")
                    self.movimientoJugador()
            else:
                print("Por favor, seleccione una casilla valida\n")
                self.movimientoJugador()
        else:
            print("Por favor, seleccione un numero\n")
            self.movimientoJugador()
        
class Persona2(TicTacToe):
    def __init__(self, fichas, matrizTablero, contadorMovimientos, modalidad, opciones, nivel, turno):
        super().__init__()

        self.palabras = ""

        self.fichas = fichas
        self.matrizTablero = matrizTablero
        self.contadorMovimientos = contadorMovimientos
        self.opciones = opciones
        self.nivel = nivel
        self.turno = turno
        self.modalidad = modalidad

    def movimientoJugador(self):
        seleccion = input(F"Seleccione casilla jugador {self.fichas[self.turno]}: ")
        if(seleccion.isdigit() == True):
            casillas = int(seleccion)
            if( (casillas > 0) and (casillas <10) ):
                filas = int((casillas - 1)/3)
                columnas = (casillas - 3*(int((casillas - 1)/3))) - 1
                if( (self.matrizTablero[filas][columnas]) == " "):
                    self.contadorMovimientos += 1
                    self.matrizTablero[filas][columnas] = self.fichas[self.turno]
                    Tablero().mostrarTablero(self.matrizTablero)
                    self.palabras = Ganador().revisarGanador(self.fichas[self.turno], self.contadorMovimientos, self.matrizTablero)
                    self.turno = int(not self.turno)

                    if(self.palabras != " "):
                        print(self.palabras)
                    else:
                        Persona1(self.fichas, self.matrizTablero, self.contadorMovimientos, self.modalidad, self.opciones, self.nivel, self.turno).movimientoJugador()

                else:
                    print("Casilla no disponible, por favor seleccione otra\n")
                    self.movimientoJugador()
            else:
                print("Por favor, seleccione una casilla valida\n")
                self.movimientoJugador()
        else:
            print("Por favor, seleccione un numero\n")
            self.movimientoJugador()


class Maquina(TicTacToe):
    def __init__(self, fichas, matrizTablero, contadorMovimientos, modalidad, opciones, nivel, turno):
        super().__init__()

        self.palabras = ""

        self.fichas = fichas
        self.matrizTablero = matrizTablero
        self.contadorMovimientos = contadorMovimientos
        self.opciones = opciones
        self.nivel = nivel
        self.turno = turno
        self.modalidad = modalidad

    def movimientoJugador(self):
        if(self.opciones[self.nivel + 2] == "FACIL"):
            print(F"Seleccionando casilla para jugador {self.fichas[self.turno]}: ")
            self.nivel1()
        elif(self.opciones[self.nivel + 2] == "INTERMEDIO"):
            self.nivel2()
        else:
            self.nivel3()

    def nivel1(self):
        casillas = random.randint(1, 9)
        filas = int((casillas - 1)/3)
        columnas = (casillas - 3*(int((casillas - 1)/3))) - 1

        if( (self.matrizTablero[filas][columnas]) == " "):
            self.contadorMovimientos += 1
            self.matrizTablero[filas][columnas] = self.fichas[self.turno]
            Tablero().mostrarTablero(self.matrizTablero)
            self.palabras = Ganador().revisarGanador(self.fichas[self.turno], self.contadorMovimientos, self.matrizTablero)
            self.turno = int(not self.turno)

            if(self.palabras != " "):
                print(self.palabras)
            else:
                Persona1(self.fichas, self.matrizTablero, self.contadorMovimientos, self.modalidad, self.opciones, self.nivel, self.turno).movimientoJugador()

        else:
            self.nivel1()

    def nivel2(self):
        pass

    def nivel3(self):
        pass

class Ganador(TicTacToe):
    def __init__(self):
        super().__init__()

    def revisarGanador(self, fichaTurno, numeroMovimiento, matrizTablero):
        if(numeroMovimiento == 9):
            return "Juego empatado"
        else:
            return self.revisarFilas(fichaTurno, matrizTablero)

    def revisarFilas(self, jugador, matrizTablero):
        for i in range(0, 3):
            if(matrizTablero[i][0] == matrizTablero[i][1] == matrizTablero[i][2] == jugador):
                return F"Juego ganado por {jugador}"

        return self.revisarColumnas(jugador, matrizTablero)

    def revisarColumnas(self, jugador, matrizTablero):
        for i in range(0, 3):
            if(matrizTablero[0][i] == matrizTablero[1][i] == matrizTablero[2][i] == jugador):
                return F"Juego ganado por {jugador}"

        return self.revisarDiagonales(jugador, matrizTablero)

    def revisarDiagonales(self, jugador, matrizTablero):
        if(matrizTablero[0][0] == matrizTablero[1][1] == matrizTablero[2][2] == jugador):
            return F"Juego ganado por {jugador}"
        elif(matrizTablero[2][0] == matrizTablero[1][1] == matrizTablero[0][2] == jugador):
            return F"Juego ganado por {jugador}"
        else:
            return " "

class Tablero(TicTacToe):
    def __init__(self):
        super().__init__()

    def inicializarTablero(self):
        matrizTablero = [[" ", " ", " "],
                         [" ", " ", " "],
                         [" ", " ", " "]]

        print("\n")
        print("            |            |         ")
        print(f"1     {matrizTablero[0][0]}     |2     {matrizTablero[0][1]}     |3     {matrizTablero[0][2]}     ")
        print("            |            |         ")
        print("---------------------------------------")
        print("            |            |         ")
        print(f"4     {matrizTablero[1][0]}     |5     {matrizTablero[1][1]}     |6     {matrizTablero[1][2]}     ")
        print("            |            |         ")
        print("---------------------------------------")
        print("            |            |         ")
        print(f"7     {matrizTablero[2][0]}     |8     {matrizTablero[2][1]}     |9     {matrizTablero[2][2]}     ")
        print("            |            |         ")
        print("\n")
        print("\n")

        return matrizTablero

    def mostrarTablero(self, matrizTablero):
        print("\n")
        print("            |            |         ")
        print(f"1     {matrizTablero[0][0]}     |2     {matrizTablero[0][1]}     |3     {matrizTablero[0][2]}     ")
        print("            |            |         ")
        print("---------------------------------------")
        print("            |            |         ")
        print(f"4     {matrizTablero[1][0]}     |5     {matrizTablero[1][1]}     |6     {matrizTablero[1][2]}     ")
        print("            |            |         ")
        print("---------------------------------------")
        print("            |            |         ")
        print(f"7     {matrizTablero[2][0]}     |8     {matrizTablero[2][1]}     |9     {matrizTablero[2][2]}     ")
        print("            |            |         ")
        print("\n")
        print("\n")

TicTacToe().jugar()