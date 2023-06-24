import random

class TicTacToe:
    def __init__(self):
        pass

    def jugar(self):
        print("BIENVENIDO AL JUEGO TIC TAC TOE\n")
        seleccion = Menu()
        seleccion.seleccionarModoDeJuego()

        if(seleccion.modalidad == "1 JUGADOR"):
            seleccion.seleccionarNivel() 
            seleccion.seleccionarFicha()
            tablero = Tablero()
            tablero.inicializarTablero()

            return self.turnos(tablero.matrizTablero, seleccion.fichas, seleccion.modalidad, seleccion.nivel)
        elif(seleccion.modalidad == "2 JUGADORES"):
            seleccion.seleccionarFicha()
            tablero = Tablero()
            tablero.inicializarTablero()

            return self.turnos(tablero.matrizTablero, seleccion.fichas, seleccion.modalidad, "")
        else:
            return print("\nJUEGO TERMINADO")

    def turnos(self, matrizTablero, fichas, modalidad, nivel):
        numeroMovimientos = 0
        turno = False
        if( (modalidad == "1 JUGADOR") ):
            if(fichas[0] == "X"):
                return Maquina().seleccionarCasilla(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)
            else:
                return Persona1().seleccionarCasilla(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, not turno)
        else:
            if(fichas[0] == "X"):
                return Persona1().seleccionarCasilla(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)
            else:
                return Persona2().seleccionarCasilla(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, not turno)

class Persona1(TicTacToe):
    def __init__(self):
        super().__init__()

        self.filas = -1
        self.columnas = -1

    def seleccionarCasilla(self, fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno):
        seleccion = input(F"Seleccione casilla jugador {fichas[turno]}: ")
        if(seleccion.isdigit() == True):
            casillas = int(seleccion)
            if( (casillas > 0) and (casillas < 10) ):
                self.filas = int((casillas - 1)/3)
                self.columnas = (casillas - 3*(int((casillas - 1)/3))) - 1
                if( (matrizTablero[self.filas][self.columnas]) == " "):
                    return self.movimientoJugador(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)
                else:
                    print("Casilla no disponible, por favor seleccione otra\n")
                    return self.seleccionarCasilla(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)
            else:
                print("Por favor, seleccione una casilla valida\n")
                return self.seleccionarCasilla(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)
        else:
            print("Por favor, seleccione un numero\n")
            return self.seleccionarCasilla(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)

    def movimientoJugador(self, fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno):
        numeroMovimientos += 1
        matrizTablero[self.filas][self.columnas] = fichas[turno]
        Tablero().mostrarTablero(matrizTablero)
        ganador = Ganador()
        ganador.revisarGanador(fichas, matrizTablero, numeroMovimientos, turno)
        resultado = ganador.resultado
        turno = int(not turno)

        if(resultado != " "):
            return print(resultado)
        else:
            if( (modalidad == "1 JUGADOR") ):
                return Maquina().seleccionarCasilla(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)
            else:
                return Persona2().seleccionarCasilla(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)

class Persona2(TicTacToe):
    def __init__(self):
        super().__init__()

        self.filas = -1
        self.columnas = -1

    def seleccionarCasilla(self, fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno):
        seleccion = input(F"Seleccione casilla jugador {fichas[turno]}: ")
        if(seleccion.isdigit() == True):
            casillas = int(seleccion)
            if( (casillas > 0) and (casillas < 10) ):
                self.filas = int((casillas - 1)/3)
                self.columnas = (casillas - 3*(int((casillas - 1)/3))) - 1
                if( (matrizTablero[self.filas][self.columnas]) == " "):
                    return self.movimientoJugador(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)
                else:
                    print("Casilla no disponible, por favor seleccione otra\n")
                    return self.seleccionarCasilla(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)
            else:
                print("Por favor, seleccione una casilla valida\n")
                return self.seleccionarCasilla(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)
        else:
            print("Por favor, seleccione un numero\n")
            return self.seleccionarCasilla(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)

    def movimientoJugador(self, fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno):
        numeroMovimientos += 1
        matrizTablero[self.filas][self.columnas] = fichas[turno]
        Tablero().mostrarTablero(matrizTablero)
        ganador = Ganador()
        ganador.revisarGanador(fichas, matrizTablero, numeroMovimientos, turno)
        resultado = ganador.resultado
        turno = int(not turno)

        if(resultado != " "):
            return print(resultado)
        else:
            return Persona2().seleccionarCasilla(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)

class Maquina(TicTacToe):
    def __init__(self):
        super().__init__()

        self.filas = -1
        self.columnas = -1

    def seleccionarCasilla(self, fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno):
        print(F"Seleccionando casilla para jugador {fichas[int(turno)]}: ")
        if(nivel == "FACIL"):
            return self.nivel1(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)
        elif(nivel == "INTERMEDIO"):
            return self.nivel2(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)
        else:
            return self.nivel3(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)

    def movimientoJugador(self, fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno):
        numeroMovimientos += 1
        matrizTablero[self.filas][self.columnas] = fichas[int(turno)]
        Tablero().mostrarTablero(matrizTablero)
        ganador = Ganador()
        ganador.revisarGanador(fichas, matrizTablero, numeroMovimientos, turno)
        resultado = ganador.resultado
        turno = int(not self.turno)

        if(resultado != " "):
            return print(resultado)
        else:
            return Persona1().seleccionarCasilla(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)

    def nivel1(self, fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno):
        ataque = Ataque()
        ataque.aleatorio(matrizTablero)
        self.filas = ataque.filas
        self.columnas = ataque.columnas
        return self.movimientoJugador(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)

    def nivel2(self, fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno):
        ataque = Ataque()
        ataque.revisarFilas(matrizTablero, fichas, turno)
        self.filas = ataque.filas
        self.columnas = ataque.columnas

        if( (self.filas == -1) and (self.columnas == -1) ):
            defensa = Defensa()
            defensa.revisarFilas(matrizTablero, fichas, turno)
            self.filas = defensa.filas
            self.columnas = defensa.columnas

            if( (self.filas == -1) and (self.columnas == -1) ):
                ataque.aleatorio(matrizTablero)
                self.filas = ataque.filas
                self.columnas = ataque.columnas
                return self.movimientoJugador(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)
            else:
                return self.movimientoJugador(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)
        else:
            return self.movimientoJugador(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)

    def nivel3(self, fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno):
        ataqueIA = AtaqueIA()
        ataqueIA.mejorJugada(fichas, matrizTablero, numeroMovimientos, turno)
        self.filas = ataqueIA.filas
        self.columnas = ataqueIA.columnas
        return self.movimientoJugador(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)

class AtaqueIA(Maquina):
    def __init__(self):
        super().__init__()

        self.filas = -1
        self.columnas = -1
        self.mejorPuntaje = 0

    def mejorJugada(self, fichas, matrizTablero, numeroMovimientos, turno):
        self.mejorPuntaje = -10000
        algoritmo = AtaqueIA()
        for i in range(0, 3):
            for j in range(0, 3):
                if(matrizTablero[i][j] == " "):
                    matrizTablero[i][j] = fichas[int(turno)]
                    numeroMovimientos += 1
                    algoritmo.minimax(fichas, matrizTablero, numeroMovimientos, turno, -10000, 10000)
                    puntaje = algoritmo.mejorPuntaje
                    matrizTablero[i][j] = " "
                    numeroMovimientos -= 1

                    if(puntaje > self.mejorPuntaje):
                        self.mejorPuntaje = puntaje
                        self.filas = i
                        self.columnas = j
        return

    def minimax(self, fichas, matrizTablero, numeroMovimientos, turno, alpha, beta):
        ganador = Ganador()
        ganador.revisarGanador(fichas, matrizTablero, numeroMovimientos, turno)

        if( (ganador.resultado == F"Juego ganado por {fichas[int(turno)]}") ):
            self.mejorPuntaje = ( -10*(int(turno)) ) + ( 10*(int(not turno)) )
            return
        elif( (ganador.resultado == F"Juego ganado por {fichas[int(not turno)]}") ):
            self.mejorPuntaje = ( -10*(int(not turno)) ) + ( 10*(int(turno)) )
            return
        elif( (ganador.resultado == "Juego empatado") ):
            self.mejorPuntaje = 0
            return

        if(turno == True):
            self.mejorPuntaje = -10000
            algoritmo = AtaqueIA()
            for i in range(0, 3):
                for j in range(0, 3):
                    if(matrizTablero[i][j] == " "):
                        matrizTablero[i][j] = fichas[int(not turno)]
                        numeroMovimientos += 1
                        algoritmo.minimax(fichas, matrizTablero, numeroMovimientos, not turno, alpha, beta)
                        puntaje = algoritmo.mejorPuntaje
                        matrizTablero[i][j] = " "
                        numeroMovimientos -= 1
                        self.mejorPuntaje = max(puntaje, self.mejorPuntaje)
                        alpha = max(alpha, self.mejorPuntaje)

                        if(beta <= alpha):
                            break
            return
        else:
            self.mejorPuntaje = 10000
            algoritmo = AtaqueIA()
            for i in range(0, 3):
                for j in range(0, 3):
                    if(matrizTablero[i][j] == " "):
                        matrizTablero[i][j] = fichas[int(not turno)]
                        numeroMovimientos += 1
                        algoritmo.minimax(fichas, matrizTablero, numeroMovimientos, not turno, alpha, beta)
                        puntaje = algoritmo.mejorPuntaje
                        matrizTablero[i][j] = " "
                        numeroMovimientos -= 1
                        self.mejorPuntaje = min(puntaje, self.mejorPuntaje)
                        beta = min(beta, self.mejorPuntaje)

                        if(beta <= alpha):
                            break
            return

class Ataque(Maquina):
    def __init__(self):
        super().__init__()

        self.filas = -1
        self.columnas = -1

    def aleatorio(self, matrizTablero):
        casillas = random.randint(1, 9)
        self.filas = int((casillas - 1)/3)
        self.columnas = (casillas - 3*(int((casillas - 1)/3))) - 1

        if( (matrizTablero[self.filas][self.columnas]) == " "):
            return
        else:
            return self.aleatorio(matrizTablero)

    def revisarFilas(self, matrizTablero, fichas, turno):
        for i in range(0, 3):
            if( ((matrizTablero[i][0] == matrizTablero[i][1] == fichas[int(turno)]) and (matrizTablero[i][2] == " ")) or 
                ((matrizTablero[i][0] == matrizTablero[i][2] == fichas[int(turno)]) and (matrizTablero[i][1] == " ")) or
                ((matrizTablero[i][1] == matrizTablero[i][2] == fichas[int(turno)]) and (matrizTablero[i][0] == " "))):
                for j in range(0, 3):
                    if(matrizTablero[i][j] == " "):
                        self.filas = i
                        self.columnas = j
                        return
        return self.revisarColumnas(matrizTablero, fichas, turno)

    def revisarColumnas(self, matrizTablero, fichas, turno):
        for i in range(0, 3):
            if( ((matrizTablero[0][i] == matrizTablero[1][i] == fichas[int(turno)]) and (matrizTablero[2][i] == " ")) or 
                ((matrizTablero[0][i] == matrizTablero[2][i] == fichas[int(turno)]) and (matrizTablero[1][i] == " ")) or
                ((matrizTablero[1][i] == matrizTablero[2][i] == fichas[int(turno)]) and (matrizTablero[0][i] == " "))):
                for j in range(0, 3):
                    if(matrizTablero[j][i] == " "):
                        self.filas = j
                        self.columnas = i
                        return
        return self.revisarDiagonales(matrizTablero, fichas, turno)

    def revisarDiagonales(self, matrizTablero, fichas, turno):
        if( ((matrizTablero[0][0] == matrizTablero[1][1] == fichas[int(turno)]) and (matrizTablero[2][2] == " ")) or
            ((matrizTablero[0][0] == matrizTablero[2][2] == fichas[int(turno)]) and (matrizTablero[1][1] == " ")) or
            ((matrizTablero[1][1] == matrizTablero[2][2] == fichas[int(turno)]) and (matrizTablero[0][0] == " "))):
            for i in range(0, 3):
                if(matrizTablero[i][i] == " "):
                    self.filas = i
                    self.columnas = i
                    return
        elif( ((matrizTablero[0][2] == matrizTablero[1][1] == fichas[int(turno)]) and (matrizTablero[2][0] == " ")) or 
              ((matrizTablero[0][2] == matrizTablero[2][0] == fichas[int(turno)]) and (matrizTablero[1][1] == " ")) or
              ((matrizTablero[1][1] == matrizTablero[2][0] == fichas[int(turno)]) and (matrizTablero[0][2] == " "))):
            for i in range(0, 3):
                if(self.matrizTablero[i][2 - i] == " "):
                    self.filas = i
                    self.columnas = 2 - i
                    return
        else:
            self.filas = -1
            self.columnas = -1
            return

class Defensa(Maquina):
    def __init__(self):
        super().__init__()

        self.filas = -1
        self.columnas = -1

    def revisarFilas(self, matrizTablero, fichas, turno):
        for i in range(0, 3):
            if( ((matrizTablero[i][0] == matrizTablero[i][1] == fichas[int(not turno)]) and (matrizTablero[i][2] == " ")) or 
                ((matrizTablero[i][0] == matrizTablero[i][2] == fichas[int(not turno)]) and (matrizTablero[i][1] == " ")) or
                ((matrizTablero[i][1] == matrizTablero[i][2] == fichas[int(not turno)]) and (matrizTablero[i][0] == " "))):
                for j in range(0, 3):
                    if(matrizTablero[i][j] == " "):
                        self.filas = i
                        self.columnas = j
                        return
        return self.revisarColumnas(matrizTablero, fichas, turno)

    def revisarColumnas(self, matrizTablero, fichas, turno):
        for i in range(0, 3):
            if( ((matrizTablero[0][i] == matrizTablero[1][i] == fichas[int(not turno)]) and (matrizTablero[2][i] == " ")) or 
                ((matrizTablero[0][i] == matrizTablero[2][i] == fichas[int(not turno)]) and (matrizTablero[1][i] == " ")) or
                ((matrizTablero[1][i] == matrizTablero[2][i] == fichas[int(not turno)]) and (matrizTablero[0][i] == " "))):
                for j in range(0, 3):
                    if(matrizTablero[j][i] == " "):
                        self.filas = j
                        self.columnas = i
                        return
        return self.revisarDiagonales(matrizTablero, fichas, turno)

    def revisarDiagonales(self, matrizTablero, fichas, turno):
        if( ((matrizTablero[0][0] == matrizTablero[1][1] == fichas[int(not turno)]) and (matrizTablero[2][2] == " ")) or 
            ((matrizTablero[0][0] == matrizTablero[2][2] == fichas[int(not turno)]) and (matrizTablero[1][1] == " ")) or
            ((matrizTablero[1][1] == matrizTablero[2][2] == fichas[int(not turno)]) and (matrizTablero[0][0] == " "))):
            for i in range(0, 3):
                if(matrizTablero[i][i] == " "):
                    self.filas = i
                    self.columnas = i
                    return
        elif( ((matrizTablero[0][2] == matrizTablero[1][1] == fichas[int(not turno)]) and (matrizTablero[2][0] == " ")) or 
              ((matrizTablero[0][2] == matrizTablero[2][0] == fichas[int(not turno)]) and (matrizTablero[1][1] == " ")) or
              ((matrizTablero[1][1] == matrizTablero[2][0] == fichas[int(not turno)]) and (matrizTablero[0][2] == " "))):
            for i in range(0, 3):
                if(matrizTablero[i][2 - i] == " "):
                    self.filas = i
                    self.columnas = 2 - i
                    return
        else:
            self.filas = -1
            self.columnas = -1
            return


class Ganador(TicTacToe):
    def __init__(self):
        self.resultado = ""

    def revisarGanador(self, fichas, matrizTablero, numeroMovimientos, turno):
        self.revisarFilas(fichas, matrizTablero, turno)
        if( (self.resultado == " ") and (numeroMovimientos == 9) ):
            self.resultado = "Juego empatado"
        return

    def revisarFilas(self, fichas, matrizTablero, turno):
        for i in range(0, 3):
            if(matrizTablero[i][0] == matrizTablero[i][1] == matrizTablero[i][2] == fichas[int(turno)]):
                self.resultado = F"Juego ganado por {fichas[int(turno)]}"
                return
        return self.revisarColumnas(fichas, matrizTablero, turno)

    def revisarColumnas(self, fichas, matrizTablero, turno):
        for i in range(0, 3):
            if(matrizTablero[0][i] == matrizTablero[1][i] == matrizTablero[2][i] == fichas[int(turno)]):
                self.resultado = F"Juego ganado por {fichas[int(turno)]}"
                return
        return self.revisarDiagonales(fichas, matrizTablero, turno)

    def revisarDiagonales(self, fichas, matrizTablero, turno):
        if(matrizTablero[0][0] == matrizTablero[1][1] == matrizTablero[2][2] == fichas[int(turno)]):
            self.resultado = F"Juego ganado por {fichas[int(turno)]}"
            return
        elif(matrizTablero[2][0] == matrizTablero[1][1] == matrizTablero[0][2] == fichas[int(turno)]):
            self.resultado = F"Juego ganado por {fichas[int(turno)]}"
            return
        else:
            self.resultado = " "
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
                return self.seleccionarModoDeJuego()
        else:
            print("Por favor, seleccione un numero\n")
            return self.seleccionarModoDeJuego()

    def seleccionarNivel(self):
        seleccion = input(F"\nSeleccione el siguiente numero para la dificultad:\n1 para {self.opciones[3]} \n2 para {self.opciones[4]} \n3 para {self.opciones[5]}\n\nDIFICULTAD DE JUEGO: ")
        if(seleccion.isdigit() == True):
            if( (int(seleccion) > 0) and (int(seleccion) < 4) ):
                self.nivel = self.opciones[int(seleccion) + 2]
                return 
            else:
                print("Por favor, seleccione una modalidad valida\n")
                return self.seleccionarNivel()
        else:
            print("Por favor, seleccione un numero\n")
            return self.seleccionarNivel()

    def seleccionarFicha(self):
        if(self.modalidad == "1 JUGADOR"):
            aleatorio = random.randint(0, 11)
            if( (aleatorio >= 0) and (aleatorio <= 5) ):
                self.fichas = ["X", "O"]
                return print("INICIA MAQUINA\n")
            else:
                self.fichas = ["O", "X"]
                return print("INICIA JUGADOR 1\n")
        else:
            ficha = (input("Seleccione ficha X / O:\n")).upper()
            if(ficha == "X"):
                self.fichas = ["X", "O"]
                return print("INICIA JUGADOR 1\n")
            elif(ficha == "O"):
                self.fichas = ["O", "X"]
                return print("INICIA JUGADOR 2\n")
            else:
                print("Por favor, seleccione una ficha valida\n")
                return self.seleccionarFicha()

TicTacToe().jugar()