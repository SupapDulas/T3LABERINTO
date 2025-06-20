import copy

laberinto = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 3, 1, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1]
]

laberinto_original = copy.deepcopy(laberinto)  

direcciones = [(-1, 0), (0, 1), (1, 0), (0, -1)]

puntos_necesarios = 23
puntos_acumulados = 0
camino = []
mejor_camino = None

def es_valido(x, y):
    return 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0])

def obtener_puntos(celda):
    if celda == 'I' or celda == 'F':
        return 1
    return celda if isinstance(celda, int) else 0

def backtracking(x, y):
    global puntos_acumulados, mejor_camino

    if laberinto[x][y] == 'F':
        if puntos_acumulados >= puntos_necesarios:
            mejor_camino = camino.copy()
        return

    temp = laberinto[x][y]
    laberinto[x][y] = -1
    puntos_acumulados += obtener_puntos(temp)
    camino.append((x, y))

    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        if es_valido(nx, ny) and laberinto[nx][ny] != 0 and laberinto[nx][ny] != -1:
            backtracking(nx, ny)

    laberinto[x][y] = temp
    puntos_acumulados -= obtener_puntos(temp)
    camino.pop()

def imprimir_laberinto():
    print("Laberinto original:")
    for fila in laberinto:
        print(" ".join(str(c) for c in fila))

def imprimir_camino(cam):
    ruta = [[' ' for _ in range(len(laberinto[0]))] for _ in range(len(laberinto))]
    for x, y in cam:
        ruta[x][y] = 'X'
    ruta[0][0] = 'F'
    ruta[len(laberinto)-1][0] = 'I'
    print("\nCamino para salir (X):")
    for fila in ruta:
        print(" ".join(fila))

def calcular_puntos(cam):
    total = 0
    for x, y in cam:
        celda = laberinto_original[x][y]  
        total += obtener_puntos(celda)
    return total

def main():
    imprimir_laberinto()
    start_x, start_y = len(laberinto)-1, 0
    backtracking(start_x, start_y)

    if mejor_camino:
        puntos = calcular_puntos(mejor_camino)
        print(f"\nSe encontró un camino con al menos {puntos_necesarios} puntos.")
        imprimir_camino(mejor_camino)
        print(f"\nPuntos logrados en el camino: {puntos}")
    else:
        print("\nNo se encontró ningún camino con la cantidad mínima de puntos requerida.")

if __name__ == "__main__":
    main()
