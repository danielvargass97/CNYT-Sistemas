import Numeros_complejos as NC
import math


def adicionVectores(v1,v2):
    '''La adicion de dos vectores complejos es posible si ambos tienen la misma
    cantidad de filas, se hace punto a punto.El resultado es un vector'''
    
    vector_respuesta = []
    try:
        a = len(v1) - len(v2)
        if a != 0:
            raise NameError('Vectores con diferentes dimensiones')
        
    except NameError:
        print("No se puede sumar los vectores porque no son compatibles")
    else:
        
        for i in range(0,len(v1)):
            vector_respuesta.append(NC.suma(v1[i],v2[i]))
            
        return vector_respuesta

def inversoAditivoVector(v):
    '''El inverso aditivo de un vector complejo es el resultado de multiplicar
    -1 a todo el vector. El resultado es un vector'''

    return multiplicacionEscalarVector([-1,0], v)

def multiplicacionEscalarVector(c,v):
    '''La multiplicacion de un escalar por un vector se realiza multiplicando
    cada punto del vector por el escalar. El resultado es un vector'''

    vector_respuesta = []
    for i in range(0, len(v)):
        vector_respuesta.append(NC.producto(c,v[i]))

    return vector_respuesta

def adicionMatrices(A,B):
    '''La adicion de matrices es posible si ambas matrices tienen el mismo
    numero de flas y de columas. El resultado es una matriz'''

    matriz_respuesta = []
    try:
        filas = len(A)-len(B)
        columnas = len(A[0]) - len(B[0])
        if filas != 0 and columnas != 0:
            raise NameError('Matrices con diferentes dimensiones')
    except NameError:
        print('No se pueden sumar las matrices porque no son compatibles')

    else:
        for i in range(0, len(A)):
            aux_fila = []
            for j in range(0, len(A[0])):
                aux_fila.append(NC.suma(A[i][j], B[i][j]))
            matriz_respuesta.append(aux_fila)

        return matriz_respuesta

def multiplicacionEscalarMatriz(c, A):
    '''La multiplicacion de un escalar por un vector se realiza multiplicando
    cada punto de la matriz por el escalar. El resultado es una matriz'''

    matriz_respuesta = []

    for i in range(0, len(A)):
            aux_fila = []
            for j in range(0, len(A[0])):
                aux_fila.append(NC.producto(c, A[i][j]))
            matriz_respuesta.append(aux_fila)

    return matriz_respuesta

def inversoAditivoMatriz(A):
    '''El inverso aditivo de una matriz compleja es el resultado de multiplicar
    -1 a toda la matriz. El resultado es una matriz'''

    return multiplicacionEscalarMatriz([-1,0],A)
    
def transpuestaMatrizCompleja(A):
    '''La transpuesta de una matriz compleja es cambiar filas por columnas.El
    Resultado es una matriz'''

    
    filas = len(A)
    columnas = len(A[0])
    matriz_respuesta = [[[0,0]]*filas for x in range(columnas)]

    for i in range(filas):
        for j in range(columnas):
            matriz_respuesta[j][i] = A[i][j]

    return matriz_respuesta

def transpuestaVectorComplejo(v):
    '''La transpuesta de un vector complejo es cambiar las filas por la columna.
    El resultado es una matriz'''

    filas = len(v)
    matriz_respuesta = [v]

    return matriz_respuesta

def conjugadaMatrizCompleja(A):
    '''La conjugada de una matriz compleja es hacer el conjugado a cada punto de
    la matriz.El resultado es una matriz'''

    filas = len(A)
    columnas = len(A[0])

    for i in range(filas):
        for j in range(columnas):
            A[i][j] = NC.conjugado(A[i][j])
    return A
    
def conjugadaVectorComplejo(v):
    '''La conjugada de un vector complejo es hacer el conjugado a cada punto del
    vector matriz.El resultado es una matriz'''

    filas = len(v)

    for i in range(filas):
        v[i] = NC.conjugado(v[i])
    return v

def adjuntaMatrizCompleja(A):
    '''La adjunta de una matriz compleja es la transpuesta de la conjugada.El
    resultado es una matriz'''

    return transpuestaMatrizCompleja(conjugadaMatrizCompleja(A))

def adjuntaVectorComplejo(v):
    '''La adjunta de un vector complejo es la transpuesta de la conjugada.El
    resultado es una matriz'''

    return transpuestaVectorComplejo(conjugadaVectorComplejo(v))

def productoMatricialComplejo(A, B):
    '''El produco de dos matrices complejas es solo posible si el numero de
    columas de A es igual al numero de filas de B, de ser asi se multiplica fila
    por columna y se suman los resultados, esto da como resultado cada punto de
    la matriz respuesta.'''


    matriz_respuesta = []
    filasA = len(A)
    columnasA = len(A[0])
    filasB = len(B)
    columnasB = len(B[0])
    try:
        if columnasA != filasB:
            raise NameError('Error. Las matrices no tienen dimensiones compatibles.')
        
    except NameError:
        print("Error. Las matrices no tienen dimensiones compatibles.")
    else:
        matriz_respuesta = [ [[0,0]]*columnasB for x in range(filasA) ]

        for i in range(filasA):
            for j in range(columnasB):
               for k in range(filasB):
                   matriz_respuesta[i][j] = NC.suma(matriz_respuesta[i][j],
                                                  NC.producto(A[i][k], B[k][j]))
        
        
        return matriz_respuesta

def accionMatrizSobreVectorComplejo(A, v):
    '''La accion de una matriz compleja sobre un vector complejos es el producto
    de de estos, cuando son compatibles (igual que en la multiplicacion matricial.
    El restultado es una vector'''

    for x in range(len(v)):
        v[x] = [v[x]]

    return productoMatricialComplejo(A, v)

def productoInternoVectoresComplejos(v1, v2):
    '''El producto interno entre dos vectores <v1,v2> es la adjunta del v1
    multiplicado por el v2. El resultado es un numero complejo'''
    
    return accionMatrizSobreVectorComplejo(adjuntaVectorComplejo(v1), v2)[0][0]

def normaVectorComplejo(v):
    '''La norma de un vector complejo es la raiz cuadrada del producto interno
    de el mismo.El resultado es un entero'''
    v1 = v
    v2 = v[:]
    
    return productoInternoVectoresComplejos(v1, v2)[0]**0.5

def distanciaVectoresComplejos(v1, v2):
    '''La distancia entre dos vectores complejos es la norma de la resta de los
    mismos.El resultado es un entero'''
    return normaVectorComplejo(adicionVectores(v1, inversoAditivoVector(v2)))

def esMatrizUnitaria(A):
    '''Identificar si una matriz es unitaria es mirar si la matria A multiplicada
    por adjunta(A) es iguual a la matriz identidad del tamaño correspondiente'''
    
    filas = len(A)
    columnas = len(A[0])

    if filas != columnas:
        return False
    else:
        I = [[[0,0]]*filas for x in range(columnas)]
        B = [[[0,0]]*filas for x in range(columnas)]
        for i in range(filas):
            for j in range(columnas):
                B[i][j] = A[i][j]
                if i == j:
                    I[i][j] = [1,0]
                    
        aux = productoMatricialComplejo(A, adjuntaMatrizCompleja(B))

        for x in range(len(A)):
            for y in range(len(A[0])):
                aux[x][y][0] = round(aux[x][y][0], 0)
        return aux == I
    
def esMatrizHermitania(A):
    '''Identificar si una matriz es hermitania es mirar si la matriz A es igual
    a la adjunta de A'''
    
    filas = len(A)
    columnas = len(A[0])
    B = [[[0,0]]*filas for x in range(columnas)]
    for i in range(filas):
            for j in range(columnas):
                B[i][j] = A[i][j]
    return adjuntaMatrizCompleja(B) == A

def productoTensorial(A,B):
    '''el producto tensorial V ⊗ W de dos espacios vectoriales V y W
    (sobre el mismo campo) es en sí mismo un espacio vectorial, dotado
    de la operación de composición bilineal, denotada por ⊗, de pares
    ordenados en el producto cartesiano V × W a V ⊗ W de una manera
    que generaliza el producto externo.'''

    filasA = len(A)
    filasB = len(B)
    columnasA = len(A[0])
    columnasB = len(B[0])
    
    matriz_respuesta = [[[0,0]]*(filasA*filasB) for o in range(columnasA*columnasB)]

    for x in range(filasA):
        for y in range(columnasA):
            aux = multiplicacionEscalarMatriz(A[x][y],B)
            for i in range(filasB):
                for j in range(columnasB):

                    matriz_respuesta[(filasB*x)+i][(columnasB*y)+j] = aux[i][j]
    return matriz_respuesta


