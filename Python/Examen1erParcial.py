from curses.ascii import isdigit


def arreglo(x):
    n = str(input("Escribe una cadena"))
    if isdigit (n): 
        n=a[x]
        print ("Se agregó al arreglo") 
        arreglo(x)
    else:
        print("No se agregó a la cadena")
        arreglo(x)


a = [0,1,2,3,4]

for x in range (0,10):
    arreglo(x)
    print("Posicion",a[x])
