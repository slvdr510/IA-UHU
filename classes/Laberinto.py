import random

class Laberinto:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.SIMBOLO_MURO = '█'
        self.SIMBOLO_ENTRADA = 'E'
        self.SIMBOLO_SALIDA = 'S'
        self.mapa = [[self.SIMBOLO_MURO for _ in range(columnas)] for _ in range(filas)]  # Mapa inicial con paredes externas
        
        self.generar_camino(1, 1)  # Generar camino desde la entrada
        self.mapa[1][1] = self.SIMBOLO_ENTRADA # Entrada
        self.mapa[filas - 2][columnas - 2] = 'S'  # Salida
    
    def generar_camino(self, start_row, start_col):
        # Creamos un camino que empieza en la posición inicial
        self.mapa[start_row][start_col] = ' '
        
        # Usamos un algoritmo de backtracking para generar el laberinto
        self.dfs(start_row, start_col)
    
    def dfs(self, fila, columna):
        # Direcciones posibles: arriba, abajo, izquierda, derecha
        direcciones = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        random.shuffle(direcciones) # Aleatorizamos el orden de las direcciones
        
        for direccion in direcciones:
            nueva_fila = fila + direccion[0]
            nueva_columna = columna + direccion[1]
            
            # Comprobamos si la nueva posición está dentro de los límites del laberinto
            if 1 <= nueva_fila < self.filas - 1 and 1 <= nueva_columna < self.columnas - 1:
                # Si la celda de destino está intacta, la transformamos en parte del camino
                if self.mapa[nueva_fila][nueva_columna] == self.SIMBOLO_MURO:
                    # Eliminamos la pared intermedia entre la posición actual y la nueva celda
                    self.mapa[(fila + nueva_fila) // 2][(columna + nueva_columna) // 2] = ' '
                    self.mapa[nueva_fila][nueva_columna] = ' '
                    # Continuamos el DFS desde la nueva posición
                    self.dfs(nueva_fila, nueva_columna)
    
    def mostrar(self):
        for fila in self.mapa:
            print(''.join(fila))

    def mostrar_camino(self):
        # Función para mostrar el camino desde self.SIMBOLO_ENTRADA hasta 'S' con el símbolo "·"
        def buscar_camino(fila, columna):
            if self.mapa[fila][columna] == 'S':
                return True
            if self.mapa[fila][columna] != ' ' and self.mapa[fila][columna] != self.SIMBOLO_ENTRADA:
                return False
            
            if self.mapa[fila][columna] != self.SIMBOLO_ENTRADA:  # No sobrescribir la entrada
                self.mapa[fila][columna] = '·'
             
            # Direcciones posibles: arriba, abajo, izquierda, derecha
            direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for direccion in direcciones:
                nueva_fila = fila + direccion[0]
                nueva_columna = columna + direccion[1]
                if buscar_camino(nueva_fila, nueva_columna):
                    return True
            
            if self.mapa[fila][columna] != self.SIMBOLO_ENTRADA:  # No desmarcar la entrada
                self.mapa[fila][columna] = ' '  # Desmarcar si no es el camino correcto
            return False
        
        buscar_camino(1, 1)
        self.mostrar()

    def resolver(self):
        # Método para resolver el laberinto y mostrar el camino desde self.SIMBOLO_ENTRADA hasta 'S'
        def buscar_camino(fila, columna):
            if self.mapa[fila][columna] == 'S':
                return True
            if self.mapa[fila][columna] != ' ' and self.mapa[fila][columna] != self.SIMBOLO_ENTRADA:
                return False
            
            if self.mapa[fila][columna] != self.SIMBOLO_ENTRADA:  # No sobrescribir la entrada
                self.mapa[fila][columna] = '·'
             
            # Direcciones posibles: arriba, abajo, izquierda, derecha
            direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for direccion in direcciones:
                nueva_fila = fila + direccion[0]
                nueva_columna = columna + direccion[1]
                if buscar_camino(nueva_fila, nueva_columna):
                    return True
            
            if self.mapa[fila][columna] != self.SIMBOLO_ENTRADA:  # No desmarcar la entrada
                self.mapa[fila][columna] = ' '  # Desmarcar si no es el camino correcto
            return False
        
        buscar_camino(1, 1)
        self.mostrar()

    def obtener_mapa(self):
        # Método para devolver el array del laberinto
        return self.mapa

if __name__ == "__main__":
    # Ejemplo de uso:
    laberinto = Laberinto(15, 30)  # Tamaño del laberinto: 15 filas y 30 columnas
    laberinto.resolver()
