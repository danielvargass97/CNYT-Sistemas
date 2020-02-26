import math

'''Se trabajara un complejo a+bi en la lista [a,b]'''
def potencia(c1,e):
    '''La potencia enésima de número complejo es otro número complejo tal que:
    Su módulo es la potencia n-ésima del módulo.
    Su argumento es n veces el argumento dado.'''
    
    mod = modulo(c1)
    arg = argumento(c1)

    mod = mod ** e
    arg = arg * e

    return polarACartesiano(mod, arg)
    

def polarACartesiano(m,a):
    '''La conversion de un numero complejo escrito en forma polar a forma cartesiana
    a+bi. Para realizar esta operacion ingresa el modulo (m) y el argumento (a)
    como parametro. Entonces tenemos que:
    a = m * cos(a) y
    b = m * sen(a)
    El argumento debe estar en radianes
    '''
    
    return [round(m*math.cos(math.radians(a)), 2),
            round(m*math.sin(math.radians(a)), 2)]


def cartesianoAPolar(c1):
    '''La conversion de un numero complejo escrito en forma cartesiana a polar.
    Para realizar esta operacion ingresa el numero complejo. Calculamos su
    modulo y argumento.'''
    return [modulo(c1),argumento(c1)]


def impresionExponencial(c1):
    '''Realizamos la impresion de un numero complejo en
    forma : |c| * e**(i * α)'''
    
    print(str(round(modulo(c1),2))+' * e **(i'+str(round(argumento(c1),2)))
    

def impresionBinomica(c1):
    '''Realizamos la impresion de un numero complejo en
    forma : a + b*i'''

    r1 = c1[0]
    i1 = c1[1]

    if i1 > 0:
        print(str(r1)+"+"+str(i1)+"i")
        
    else:
        print(str(r1)+""+str(i1)+"i")
        

def argumento(c1):
    '''El argumento de un numero compejo α es un numero real tal que:
    α = tan-1(b/a)'''

    r1 = c1[0]
    i1 = c1[1]

    return math.degrees(math.atan2(i1,r1))
    

def modulo(c1):
    '''El argumento de un numero compejo |z| es un numero real tal que:
    |z| = [(a**2)+(b**2)]**0.5 '''
   
    r1 = c1[0]
    i1 = c1[1]
    
    return ((r1**2)+(i1**2))**(1/2)


def conjugado(c1):
    '''El conjugado de un número complejo z es el número complejo que se obtiene
    por simetría del dado respecto del eje de abscisas.
    Representando el número complejo a + bi  y haciendo la correspondiente
    simetría, se tiene que su conjugado es a - bi '''

    r1 = c1[0]
    i1 = c1[1]

    return [r1,-i1]


def division(c1, c2):
    '''La division dos complejos la realizamos multiplicando el numerador y el
    denominador por el conjugado del denominador, así el denominador pasará a
    ser un número real.
    Finalmente se separan la parte real y la parte imaginaria. '''

    r1 = c1[0]
    r2 = c2[0]
    
    i1 = c1[1]
    i2 = c2[1]

    #Revisar que no estemos dividiendo por cero (0).

    if r2 == 0 and i2 == 0:
        return None

    #Revisamos si alguna parte (la real o la imaginaria) del denominador es
    #cero (0), ya que si alguno lo es, esto nos facilita los calculos, de ser
    #asi retornamos la respuesta

    elif r2 == 0 and i2 != 0:
        
        r3 = i1/i2
        i3 = r1/i2
        return [r3, i3]

    elif r2 != 0 and i2 == 0:

        r3 = r1/r2
        i3 = i2/r2
        return [r3, i3]
    
    else:
        z = conjugado(c2)
        numerador = producto(c1, z)
        denominador = producto(c2, z)
        return [round(numerador[0]/denominador[0],2),
                round(numerador[1]/denominador[0],2)]
        
        
def producto(c1, c2):
    '''La multiplicacion de dos complejos la realizamos de manera distributiva.
    Sumamos reales con reales e imaginarios con imaginarios.'''

    r1 = c1[0]
    r2 = c2[0]

    i1 = c1[1]
    i2 = c2[1]

    r3 = r1 * r2
    r4 = i1 * i2
    
    i3 = r1 * i2
    i4 = i1 * r2

    #Multiplicamos r4 por (-1) ya que este resultado siempre nos dara un i**2

    r4 = r4 * (-1)
    
    return [r3+r4, i3+i4]
    

def resta(c1, c2):
    '''La resta de dos complejos la realizamos de la misma forma que una resta
    de dos numeros reales. Restamos reales con reales e imaginarios con
    imaginarios.'''

    r1 = c1[0]
    r2 = c2[0]

    i1 = c1[1]
    i2 = c2[1]

    return [r1-r2, i1-i2]



def suma(c1, c2):
    '''La suma de dos complejos la realizamos de la misma forma que una sma
    de dos numeros reales. Sumamos reales con reales e imaginarios con
    imaginarios.'''

    r1 = c1[0]
    r2 = c2[0]

    i1 = c1[1]
    i2 = c2[1]

    return [r1+r2, i1+i2]

'''
#En el main del programa definimos los numeros complejos que utilizaremos
#y llamamos el metodo correspondiete a la operacion a ejecutar.
def main():
    
    complejo1 = [1,1]
    complejo2 = [3,2]
    modulo = 1.414213562370951 # 1+i
    argumento = 45.0 # 1+i
    # suma(complejo1, complejo2)
    # resta(complejo1, complejo2)
    # producto(complejo1, complejo2)
    # division(complejo1, complejo2)
    # conjugado (complejo1)
    # modulo(complejo1)
    # impresionBinomica(complejo2)
    # impresionExponencial(complejo2)
    # cartesianoAPolar(complejo1)
    # polarACartesiano(modulo, argumento)
    # potencia(complejo1, 10)
    
main()
'''

      
