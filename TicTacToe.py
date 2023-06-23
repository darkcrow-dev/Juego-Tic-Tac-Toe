import random

class TicTacToe:
    def __init__(self):
        self.numeroMovimientos = 0
        self.turno = False

    def jugar(self):
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
        if( (modalidad == "1 JUGADOR") ):
            if(fichas[0] == "X"):
                return Maquina(fichas, matrizTablero, self.numeroMovimientos, modalidad, nivel, self.turno).seleccionarCasilla()
            else:
                self.turno = int(not self.turno)
                return Persona1(fichas, matrizTablero, self.numeroMovimientos, modalidad, nivel, self.turno).seleccionarCasilla()
        else:
            if(fichas[0] == "X"):
                return Persona1(fichas, matrizTablero, self.numeroMovimientos, modalidad, nivel, self.turno).seleccionarCasilla()
            else:
                self.turno = int(not self.turno)
                return Persona2(fichas, matrizTablero, self.numeroMovimientos, modalidad, nivel, self.turno).seleccionarCasilla()

class Persona1(TicTacToe):
    def __init__(self, fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno):
        super().__init__()

        self.fichas = fichas
        self.matrizTablero = matrizTablero
        self.numeroMovimientos = numeroMovimientos
        self.modalidad = modalidad
        self.nivel = nivel
        self.turno = turno
        
        self.filas = -1
        self.columnas = -1

    def seleccionarCasilla(self):
        seleccion = input(F"Seleccione casilla jugador {self.fichas[self.turno]}: ")
        if(seleccion.isdigit() == True):
            casillas = int(seleccion)
            if( (casillas > 0) and (casillas < 10) ):
                self.filas = int((casillas - 1)/3)
                self.columnas = (casillas - 3*(int((casillas - 1)/3))) - 1
                if( (self.matrizTablero[self.filas][self.columnas]) == " "):
                    return self.movimientoJugador()
                else:
                    print("Casilla no disponible, por favor seleccione otra\n")
                    return self.seleccionarCasilla()
            else:
                print("Por favor, seleccione una casilla valida\n")
                return self.seleccionarCasilla()
        else:
            print("Por favor, seleccione un numero\n")
            return self.seleccionarCasilla()

    def movimientoJugador(self):
        self.numeroMovimientos += 1
        self.matrizTablero[self.filas][self.columnas] = self.fichas[self.turno]
        Tablero().mostrarTablero(self.matrizTablero)
        ganador = Ganador(self.fichas, self.matrizTablero, self.numeroMovimientos, self.turno)
        ganador.revisarGanador()
        palabras = ganador.palabras
        self.turno = int(not self.turno)

        if(palabras != " "):
            return print(palabras)
        else:
            if( (self.modalidad == "1 JUGADOR") ):
                return Maquina(self.fichas, self.matrizTablero, self.numeroMovimientos, self.modalidad, self.nivel, self.turno).seleccionarCasilla()
            else:
                return Persona2(self.fichas, self.matrizTablero, self.numeroMovimientos, self.modalidad, self.nivel, self.turno).seleccionarCasilla()
        
class Persona2(TicTacToe):
    def __init__(self, fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno):
        super().__init__()

        self.fichas = fichas
        self.matrizTablero = matrizTablero
        self.numeroMovimientos = numeroMovimientos
        self.nivel = nivel
        self.turno = turno
        self.modalidad = modalidad

        self.filas = -1
        self.columnas = -1

    def seleccionarCasilla(self):
        seleccion = input(F"Seleccione casilla jugador {self.fichas[self.turno]}: ")
        if(seleccion.isdigit() == True):
            casillas = int(seleccion)
            if( (casillas > 0) and (casillas < 10) ):
                self.filas = int((casillas - 1)/3)
                self.columnas = (casillas - 3*(int((casillas - 1)/3))) - 1
                if( (self.matrizTablero[self.filas][self.columnas]) == " "):
                    return self.movimientoJugador()
                else:
                    print("Casilla no disponible, por favor seleccione otra\n")
                    return self.seleccionarCasilla()
            else:
                print("Por favor, seleccione una casilla valida\n")
                return self.seleccionarCasilla()
        else:
            print("Por favor, seleccione un numero\n")
            return self.seleccionarCasilla()

    def movimientoJugador(self):
        self.numeroMovimientos += 1
        self.matrizTablero[self.filas][self.columnas] = self.fichas[self.turno]
        Tablero().mostrarTablero(self.matrizTablero)
        ganador = Ganador(self.fichas, self.matrizTablero, self.numeroMovimientos, self.turno)
        ganador.revisarGanador()
        palabras = ganador.palabras
        self.turno = int(not self.turno)

        if(palabras != " "):
            return print(palabras)
        else:
            return Persona1(self.fichas, self.matrizTablero, self.numeroMovimientos, self.modalidad, self.nivel, self.turno).seleccionarCasilla()

class Maquina(TicTacToe):
    def __init__(self, fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno):
        super().__init__()

        self.fichas = fichas
        self.matrizTablero = matrizTablero
        self.numeroMovimientos = numeroMovimientos
        self.nivel = nivel
        self.turno = turno
        self.modalidad = modalidad

        self.filas = -1
        self.columnas = -1
        self.profundidad = 0
        self.alpha = -10000
        self.beta = 10000

    def seleccionarCasilla(self):
        print(F"Seleccionando casilla para jugador {self.fichas[int(self.turno)]}: ")
        if(self.nivel == "FACIL"):
            return self.nivel1()
        elif(self.nivel == "INTERMEDIO"):
            return self.nivel2()
        else:
            return self.nivel3()

    def movimientoJugador(self):
        self.numeroMovimientos += 1
        self.matrizTablero[self.filas][self.columnas] = self.fichas[int(self.turno)]
        Tablero().mostrarTablero(self.matrizTablero)
        ganador = Ganador(self.fichas, self.matrizTablero, self.numeroMovimientos, self.turno)
        ganador.revisarGanador()
        palabras = ganador.palabras
        self.turno = int(not self.turno)

        if(palabras != " "):
            return print(palabras)
        else:
            return Persona1(self.fichas, self.matrizTablero, self.numeroMovimientos, self.modalidad, self.nivel, self.turno).seleccionarCasilla()

    def nivel1(self):
        ataque = Ataque(self.fichas, self.matrizTablero, self.numeroMovimientos, self.modalidad, self.nivel, self.turno)
        ataque.aleatorio()
        self.filas = ataque.filas
        self.columnas = ataque.columnas
        return self.movimientoJugador()

    def nivel2(self):
        ataque = Ataque(self.fichas, self.matrizTablero, self.numeroMovimientos, self.modalidad, self.nivel, self.turno)
        ataque.revisarFilas()
        self.filas = ataque.filas
        self.columnas = ataque.columnas

        if( (self.filas == -1) and (self.columnas == -1) ):
            defensa = Defensa(self.fichas, self.matrizTablero, self.numeroMovimientos, self.modalidad, self.nivel, self.turno)
            defensa.revisarFilas()
            self.filas = defensa.filas
            self.columnas = defensa.columnas

            if( (self.filas == -1) and (self.columnas == -1) ):
                ataque.aleatorio()
                self.filas = ataque.filas
                self.columnas = ataque.columnas
                return self.movimientoJugador()
            else:
                return self.movimientoJugador()
        else:
            return self.movimientoJugador()

    def nivel3(self):
        ataqueIA = AtaqueIA(self.fichas, self.matrizTablero, self.numeroMovimientos, self.modalidad, self.nivel, self.turno, self.profundidad, self.alpha, self.beta)
        ataqueIA.mejorJugada()
        self.filas = ataqueIA.filas
        self.columnas = ataqueIA.columnas
        return self.movimientoJugador()

class Ataque(Maquina):
    def __init__(self, fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno):
        super().__init__(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)
        self.filas = -1
        self.columnas = -1

    def aleatorio(self):
        casillas = random.randint(1, 9)
        self.filas = int((casillas - 1)/3)
        self.columnas = (casillas - 3*(int((casillas - 1)/3))) - 1

        if( (self.matrizTablero[self.filas][self.columnas]) == " "):
            return
        else:
            return self.aleatorio()

    def revisarFilas(self):
        for i in range(0, 3):
            if( ((self.matrizTablero[i][0] == self.matrizTablero[i][1] == self.fichas[int(self.turno)]) and (self.matrizTablero[i][2] == " ")) or 
                ((self.matrizTablero[i][0] == self.matrizTablero[i][2] == self.fichas[int(self.turno)]) and (self.matrizTablero[i][1] == " ")) or
                ((self.matrizTablero[i][1] == self.matrizTablero[i][2] == self.fichas[int(self.turno)]) and (self.matrizTablero[i][0] == " "))):
                for j in range(0, 3):
                    if(self.matrizTablero[i][j] == " "):
                        self.filas = i
                        self.columnas = j
                        return
        return self.revisarColumnas()

    def revisarColumnas(self):
        for i in range(0, 3):
            if( ((self.matrizTablero[0][i] == self.matrizTablero[1][i] == self.fichas[int(self.turno)]) and (self.matrizTablero[2][i] == " ")) or 
                ((self.matrizTablero[0][i] == self.matrizTablero[2][i] == self.fichas[int(self.turno)]) and (self.matrizTablero[1][i] == " ")) or
                ((self.matrizTablero[1][i] == self.matrizTablero[2][i] == self.fichas[int(self.turno)]) and (self.matrizTablero[0][i] == " "))):
                for j in range(0, 3):
                    if(self.matrizTablero[j][i] == " "):
                        self.filas = j
                        self.columnas = i
                        return
        return self.revisarDiagonales()

    def revisarDiagonales(self):
        if( ((self.matrizTablero[0][0] == self.matrizTablero[1][1] == self.fichas[int(self.turno)]) and (self.matrizTablero[2][2] == " ")) or
            ((self.matrizTablero[0][0] == self.matrizTablero[2][2] == self.fichas[int(self.turno)]) and (self.matrizTablero[1][1] == " ")) or
            ((self.matrizTablero[1][1] == self.matrizTablero[2][2] == self.fichas[int(self.turno)]) and (self.matrizTablero[0][0] == " "))):
            for i in range(0, 3):
                if(self.matrizTablero[i][i] == " "):
                    self.filas = i
                    self.columnas = i
                    return
        elif( ((self.matrizTablero[0][2] == self.matrizTablero[1][1] == self.fichas[int(self.turno)]) and (self.matrizTablero[2][0] == " ")) or 
              ((self.matrizTablero[0][2] == self.matrizTablero[2][0] == self.fichas[int(self.turno)]) and (self.matrizTablero[1][1] == " ")) or
              ((self.matrizTablero[1][1] == self.matrizTablero[2][0] == self.fichas[int(self.turno)]) and (self.matrizTablero[0][2] == " "))):
            for i in range(0, 3):
                if(self.matrizTablero[i][2 - i] == " "):
                    self.filas = i
                    self.columnas = 2 - i
                    return
        else:
            self.filas = -1
            self.columnas = -1
            return

class AtaqueIA(Maquina):
    def __init__(self, fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno, profundidad, alpha, beta):
        super().__init__(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)
        self.matrizTablero = matrizTablero
        self.profundidad = profundidad
        self.modalidad = modalidad
        self.turno = turno
        self.modalidad = modalidad
        self.numeroMovimientos = numeroMovimientos
        self.fichas = fichas
        self.alpha = alpha
        self.beta = beta
        self.mejorPuntaje = 0

        self.filas = -1
        self.columnas = -1

    def mejorJugada(self):
        self.mejorPuntaje = -10000
        for i in range(0, 3):
            for j in range(0, 3):
                if(self.matrizTablero[i][j] == " "):
                    self.matrizTablero[i][j] = self.fichas[int(self.turno)]
                    self.numeroMovimientos += 1
                    algoritmo = AtaqueIA(self.fichas, self.matrizTablero, self.numeroMovimientos, self.modalidad, self.nivel, self.turno, self.profundidad, self.alpha, self.beta)
                    algoritmo.minimax()
                    puntaje = algoritmo.mejorPuntaje
                    self.matrizTablero[i][j] = " "
                    self.numeroMovimientos -= 1

                    if(puntaje > self.mejorPuntaje):
                        self.mejorPuntaje = puntaje
                        self.filas = i
                        self.columnas = j
        return

    def minimax(self):
        ganador = Ganador(self.fichas, self.matrizTablero, self.numeroMovimientos, self.turno)
        ganador.revisarGanador()

        if( (ganador.palabras == F"Juego ganado por {self.fichas[int(self.turno)]}") ):
            self.mejorPuntaje = ( -10*(int(self.turno)) ) + ( 10*(int(not self.turno)) )
            return
        elif( (ganador.palabras == F"Juego ganado por {self.fichas[int(not self.turno)]}") ):
            self.mejorPuntaje = ( -10*(int(not self.turno)) ) + ( 10*(int(self.turno)) )
            return
        elif( (ganador.palabras == "Juego empatado") ):
            self.mejorPuntaje = 0
            return

        if(self.turno == True):
            self.mejorPuntaje = -10000
            for i in range(0, 3):
                for j in range(0, 3):
                    if(self.matrizTablero[i][j] == " "):
                        self.matrizTablero[i][j] = self.fichas[int(not self.turno)]
                        self.numeroMovimientos += 1
                        algoritmo = AtaqueIA(self.fichas, self.matrizTablero, self.numeroMovimientos, self.modalidad, self.nivel, not self.turno, self.profundidad + 1, self.alpha, self.beta)
                        algoritmo.minimax()
                        puntaje = algoritmo.mejorPuntaje
                        self.matrizTablero[i][j] = " "
                        self.numeroMovimientos -= 1
                        self.mejorPuntaje = max(puntaje, self.mejorPuntaje)
                        self.alpha = max(self.alpha, self.mejorPuntaje)

                        if(self.beta <= self.alpha):
                            break
            return
        else:
            self.mejorPuntaje = 10000
            for i in range(0, 3):
                for j in range(0, 3):
                    if(self.matrizTablero[i][j] == " "):
                        self.matrizTablero[i][j] = self.fichas[int(not self.turno)]
                        self.numeroMovimientos += 1
                        algoritmo = AtaqueIA(self.fichas, self.matrizTablero, self.numeroMovimientos, self.modalidad, self.nivel, not self.turno, self.profundidad + 1, self.alpha, self.beta)
                        algoritmo.minimax()
                        puntaje = algoritmo.mejorPuntaje
                        self.matrizTablero[i][j] = " "
                        self.numeroMovimientos -= 1
                        self.mejorPuntaje = min(puntaje, self.mejorPuntaje)
                        self.beta = min(self.beta, self.mejorPuntaje)

                        if(self.beta <= self.alpha):
                            break
            return

class Defensa(Maquina):
    def __init__(self, fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno):
        super().__init__(fichas, matrizTablero, numeroMovimientos, modalidad, nivel, turno)
        self.filas = -1
        self.columnas = -1

    def revisarFilas(self):
        for i in range(0, 3):
            if( ((self.matrizTablero[i][0] == self.matrizTablero[i][1] == self.fichas[int(not self.turno)]) and (self.matrizTablero[i][2] == " ")) or 
                ((self.matrizTablero[i][0] == self.matrizTablero[i][2] == self.fichas[int(not self.turno)]) and (self.matrizTablero[i][1] == " ")) or
                ((self.matrizTablero[i][1] == self.matrizTablero[i][2] == self.fichas[int(not self.turno)]) and (self.matrizTablero[i][0] == " "))):
                for j in range(0, 3):
                    if(self.matrizTablero[i][j] == " "):
                        self.filas = i
                        self.columnas = j
                        return
        return self.revisarColumnas()

    def revisarColumnas(self):
        for i in range(0, 3):
            if( ((self.matrizTablero[0][i] == self.matrizTablero[1][i] == self.fichas[int(not self.turno)]) and (self.matrizTablero[2][i] == " ")) or 
                ((self.matrizTablero[0][i] == self.matrizTablero[2][i] == self.fichas[int(not self.turno)]) and (self.matrizTablero[1][i] == " ")) or
                ((self.matrizTablero[1][i] == self.matrizTablero[2][i] == self.fichas[int(not self.turno)]) and (self.matrizTablero[0][i] == " "))):
                for j in range(0, 3):
                    if(self.matrizTablero[j][i] == " "):
                        self.filas = j
                        self.columnas = i
                        return
        return self.revisarDiagonales()

    def revisarDiagonales(self):
        if( ((self.matrizTablero[0][0] == self.matrizTablero[1][1] == self.fichas[int(not self.turno)]) and (self.matrizTablero[2][2] == " ")) or 
            ((self.matrizTablero[0][0] == self.matrizTablero[2][2] == self.fichas[int(not self.turno)]) and (self.matrizTablero[1][1] == " ")) or
            ((self.matrizTablero[1][1] == self.matrizTablero[2][2] == self.fichas[int(not self.turno)]) and (self.matrizTablero[0][0] == " "))):
            for i in range(0, 3):
                if(self.matrizTablero[i][i] == " "):
                    self.filas = i
                    self.columnas = i
                    return
        elif( ((self.matrizTablero[0][2] == self.matrizTablero[1][1] == self.fichas[int(not self.turno)]) and (self.matrizTablero[2][0] == " ")) or 
              ((self.matrizTablero[0][2] == self.matrizTablero[2][0] == self.fichas[int(not self.turno)]) and (self.matrizTablero[1][1] == " ")) or
              ((self.matrizTablero[1][1] == self.matrizTablero[2][0] == self.fichas[int(not self.turno)]) and (self.matrizTablero[0][2] == " "))):
            for i in range(0, 3):
                if(self.matrizTablero[i][2 - i] == " "):
                    self.filas = i
                    self.columnas = 2 - i
                    return
        else:
            self.filas = -1
            self.columnas = -1
            return

class Ganador(TicTacToe):
    def __init__(self, fichas, matrizTablero, numeroMovimientos, turno):
        super().__init__()
        self.palabras = ""
        self.fichas = fichas
        self.matrizTablero = matrizTablero
        self.numeroMovimientos = numeroMovimientos
        self.turno = turno

    def revisarGanador(self):
        self.revisarFilas()
        if( (self.palabras == " ") and (self.numeroMovimientos == 9) ):
            self.palabras = "Juego empatado"
        return

    def revisarFilas(self):
        for i in range(0, 3):
            if(self.matrizTablero[i][0] == self.matrizTablero[i][1] == self.matrizTablero[i][2] == self.fichas[int(self.turno)]):
                self.palabras = F"Juego ganado por {self.fichas[int(self.turno)]}"
                return
        return self.revisarColumnas()

    def revisarColumnas(self):
        for i in range(0, 3):
            if(self.matrizTablero[0][i] == self.matrizTablero[1][i] == self.matrizTablero[2][i] == self.fichas[int(self.turno)]):
                self.palabras = F"Juego ganado por {self.fichas[int(self.turno)]}"
                return
        return self.revisarDiagonales()

    def revisarDiagonales(self):
        if(self.matrizTablero[0][0] == self.matrizTablero[1][1] == self.matrizTablero[2][2] == self.fichas[int(self.turno)]):
            self.palabras = F"Juego ganado por {self.fichas[int(self.turno)]}"
            return
        elif(self.matrizTablero[2][0] == self.matrizTablero[1][1] == self.matrizTablero[0][2] == self.fichas[int(self.turno)]):
            self.palabras = F"Juego ganado por {self.fichas[int(self.turno)]}"
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
            aleatorio = random.randint(0, 10)
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