import random

class TicTacToe:
    def __init__(self):
        self.contadorMovimientos = 0
        self.turno = False

    def jugar(self):
        seleccion = Menu()
        seleccion.seleccionarModoDeJuego()

        if(seleccion.modalidad == "1 JUGADOR"):
            seleccion.seleccionarNivel() 
            seleccion.seleccionarFicha()
            tablero = Tablero()
            tablero.inicializarTablero()

            self.turnos(tablero.matrizTablero, seleccion.fichas, seleccion.modalidad, seleccion.nivel)
        elif(seleccion.modalidad == "2 JUGADORES"):
            seleccion.seleccionarFicha()
            tablero = Tablero()
            tablero.inicializarTablero()

            self.turnos(tablero.matrizTablero, seleccion.fichas, seleccion.modalidad, "")

        else:
            print("\nJUEGO TERMINADO")

    def turnos(self, matrizTablero, fichas, modalidad, nivel):
        if( (modalidad == "1 JUGADOR") ):
            if(fichas[0] == "X"):
                Maquina(fichas, matrizTablero, self.contadorMovimientos, modalidad, nivel, self.turno).movimientoJugador()
            else:
                self.turno = int(not self.turno)
                Persona1(fichas, matrizTablero, self.contadorMovimientos, modalidad, nivel, self.turno).movimientoJugador()
        else:
            if(fichas[0] == "X"):
                Persona1(fichas, matrizTablero, self.contadorMovimientos, modalidad, nivel, self.turno).movimientoJugador()
            else:
                self.turno = int(not self.turno)
                Persona2(fichas, matrizTablero, self.contadorMovimientos, modalidad, nivel, self.turno).movimientoJugador()

class Persona1(TicTacToe):
    def __init__(self, fichas, matrizTablero, contadorMovimientos, modalidad, nivel, turno):
        super().__init__()

        self.fichas = fichas
        self.matrizTablero = matrizTablero
        self.contadorMovimientos = contadorMovimientos
        self.modalidad = modalidad
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
                    ganador = Ganador()
                    ganador.revisarGanador(self.fichas[self.turno], self.contadorMovimientos, self.matrizTablero)
                    palabras = ganador.palabras
                    self.turno = int(not self.turno)

                    if(palabras != " "):
                        print(palabras)
                    else:
                        if( (self.modalidad == "1 JUGADOR") ):
                            Maquina(self.fichas, self.matrizTablero, self.contadorMovimientos, self.modalidad, self.nivel, self.turno).movimientoJugador()
                        else:
                            Persona2(self.fichas, self.matrizTablero, self.contadorMovimientos, self.modalidad, self.nivel, self.turno).movimientoJugador()

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
    def __init__(self, fichas, matrizTablero, contadorMovimientos, modalidad, nivel, turno):
        super().__init__()

        self.fichas = fichas
        self.matrizTablero = matrizTablero
        self.contadorMovimientos = contadorMovimientos
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
                    ganador = Ganador()
                    ganador.revisarGanador(self.fichas[self.turno], self.contadorMovimientos, self.matrizTablero)
                    palabras = ganador.palabras
                    self.turno = int(not self.turno)

                    if(palabras != " "):
                        print(palabras)
                    else:
                        Persona1(self.fichas, self.matrizTablero, self.contadorMovimientos, self.modalidad, self.nivel, self.turno).movimientoJugador()

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
    def __init__(self, fichas, matrizTablero, contadorMovimientos, modalidad, nivel, turno):
        super().__init__()

        self.fichas = fichas
        self.matrizTablero = matrizTablero
        self.contadorMovimientos = contadorMovimientos
        self.nivel = nivel
        self.turno = turno
        self.modalidad = modalidad

    def movimientoJugador(self):
        if(self.nivel == "FACIL"):
            print(F"Seleccionando casilla para jugador {self.fichas[self.turno]}: ")
            self.nivel1()
        elif(self.nivel == "INTERMEDIO"):
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
            ganador = Ganador()
            ganador.revisarGanador(self.fichas[self.turno], self.contadorMovimientos, self.matrizTablero)
            palabras = ganador.palabras
            self.turno = int(not self.turno)

            if(palabras != " "):
                print(palabras)
            else:
                Persona1(self.fichas, self.matrizTablero, self.contadorMovimientos, self.modalidad, self.nivel, self.turno).movimientoJugador()

        else:
            self.nivel1()

    def nivel2(self):
        pass

    def nivel3(self):
        pass

class Ganador(TicTacToe):
    def __init__(self):
        super().__init__()
        self.palabras = ""

    def revisarGanador(self, fichaTurno, numeroMovimiento, matrizTablero):
        self.revisarFilas(fichaTurno, matrizTablero)
        if( (self.palabras == " ") and (numeroMovimiento == 9) ):
            self.palabras = "Juego empatado"
        return

    def revisarFilas(self, jugador, matrizTablero):
        for i in range(0, 3):
            if(matrizTablero[i][0] == matrizTablero[i][1] == matrizTablero[i][2] == jugador):
                self.palabras = F"Juego ganado por {jugador}"
                return

        return self.revisarColumnas(jugador, matrizTablero)

    def revisarColumnas(self, jugador, matrizTablero):
        for i in range(0, 3):
            if(matrizTablero[0][i] == matrizTablero[1][i] == matrizTablero[2][i] == jugador):
                self.palabras = F"Juego ganado por {jugador}"
                return
        return self.revisarDiagonales(jugador, matrizTablero)

    def revisarDiagonales(self, jugador, matrizTablero):
        if(matrizTablero[0][0] == matrizTablero[1][1] == matrizTablero[2][2] == jugador):
            self.palabras = F"Juego ganado por {jugador}"
            return
        elif(matrizTablero[2][0] == matrizTablero[1][1] == matrizTablero[0][2] == jugador):
            self.palabras = F"Juego ganado por {jugador}"
            return
        else:
            self.palabras = " "
            return

class Tablero(TicTacToe):
    def __init__(self):
        super().__init__()
        self.matrizTablero = [[]]

    def inicializarTablero(self):
        self.matrizTablero = [[" ", " ", " "],
                              [" ", " ", " "],
                              [" ", " ", " "]]

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

        return

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

        return

class Menu(TicTacToe):
    def __init__(self):
        super().__init__()
        self.opciones = ["1 JUGADOR", "2 JUGADORES", "SALIR", "FACIL", "INTERMEDIO", "DIFICIL"]
        self.modalidad = ""
        self.nivel = ""
        self.fichas = [" ", " "]

    def seleccionarModoDeJuego(self):
        seleccion = input(F"Seleccione el siguiente numero para la modalidad:\n1 para {self.opciones[0]} \n2 para {self.opciones[1]} \n3 para {self.opciones[2]}\n\nMODO DE JUEGO: ")
        if(seleccion.isdigit() == True):
            if( (int(seleccion) > 0) and (int(seleccion) < 4) ):
                self.modalidad = self.opciones[int(seleccion) - 1]
                return 
            else:
                print("Por favor, seleccione una modalidad valida\n")
                self.seleccionarModoDeJuego()
        else:
            print("Por favor, seleccione un numero\n")
            self.seleccionarModoDeJuego()

    def seleccionarNivel(self):
        seleccion = input(F"\nSeleccione el siguiente numero para la dificultad:\n1 para {self.opciones[3]} \n2 para {self.opciones[4]} \n3 para {self.opciones[5]}\n\nDIFICULTAD DE JUEGO: ")
        if(seleccion.isdigit() == True):
            if( (int(seleccion) > 0) and (int(seleccion) < 4) ):
                self.nivel = self.opciones[int(seleccion) + 2]
                return 
            else:
                print("Por favor, seleccione una modalidad valida\n")
                self.seleccionarNivel()
        else:
            print("Por favor, seleccione un numero\n")
            self.seleccionarNivel()

    def seleccionarFicha(self):
        if(self.modalidad == "1 JUGADOR"):
            aleatorio = random.randint(1, 10)
            if( (aleatorio > 0) and (aleatorio < 5) ):
                self.fichas = ["X", "O"]
                print("INICIA MAQUINA\n")
                return
            else:
                self.fichas = ["O", "X"]
                print("INICIA JUGADOR 1\n")
                return
        else:
            ficha = (input("Seleccione ficha X / O:\n")).upper()
            if(ficha == "X"):
                self.fichas = ["X", "O"]
                print("INICIA JUGADOR 1\n")
                return
            elif(ficha == "O"):
                self.fichas = ["O", "X"]
                print("INICIA JUGADOR 2\n")
                return
            else:
                print("Por favor, seleccione una ficha valida\n")
                self.seleccionarFicha()

TicTacToe().jugar()