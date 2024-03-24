import numpy as np
opcion=1
while opcion >= 1 and opcion <= 8:
    print("--------MENU DE LA CALCULADORA-------")
    print("[1]  Suma de matrices")
    print("[2]  Resta de matrices")
    print("[3]  Producto de matriz con una escalar")
    print("[4]  Multiplicacion de matrices")
    print("[5]  Traspuesta de una matriz")
    print("[6]  Inversa de una matriz")
    print("[7]  Rango de la matriz")
    print("[8]  Determinante de una matriz")
    opcion=int(input("Escoje una opcion: "))

    if opcion==int(1):
#-----------------------------------------------------------------------------------------------------------------------------------------
#--------------OPCION 1-------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------

        print("SUMA DE MATRICES")
        f1=int(input("Ingrese numero de filas de Matriz A: "))
        c1=int(input("Ingrese numero de columnas de Matriz A: "))
        f2=int(input("Ingrese numero de filas de Matriz B: "))
        c2=int(input("Ingrese numero de columnas de Matriz B: "))
        if f1==f2 and c1==c2:
            print("------INGRESO DE DATOS------")
            A=np.empty((f1,c1))
            B=np.empty((f2,c2))
            C=np.empty((f1,c1))
            print("Matriz A")
            for i in range(f1):
                for j in range(c1):
                    dato=float(input("Ingrese el valor de ["+str(i+1)+"]["+str(j+1)+"]: "))
                    A[i][j]=dato
            print("Matriz B")
            for i in range(f2):
                for j in range(c2):
                    dato=float(input("Ingrese el valor de ["+str(i+1)+"]["+str(j+1)+"]: "))
                    B[i][j]=dato
                    C[i][j]=A[i][j]+B[i][j]
            print()
            print("Matriz A:")
            print(A)
            print("Matriz B:")
            print(B)
            print("-----RESULTADO-----")
            print(C)
            print()
            print("        -----FIN DE SUMA DE MATRICES------")        
        else:
            print("----NO SE PUEDE SUMAR LAS MATRICES----")
            break




    else:
        if opcion==int(2):
#-----------------------------------------------------------------------------------------------------------------------------------------
#--------------OPCION 2-------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------
            print("RESTA DE MATRICES")
            f1=int(input("Ingrese numero de filas de Matriz A: "))
            c1=int(input("Ingrese numero de columnas de Matriz A: "))
            f2=int(input("Ingrese numero de filas de Matriz B: "))
            c2=int(input("Ingrese numero de columnas de Matriz B: "))
            if f1==f2 and c1==c2:
                print("------INGRESO DE DATOS------")
                A=np.empty((f1,c1))
                B=np.empty((f2,c2))
                C=np.empty((f1,c1))
                print("Matriz A")
                for i in range(f1):
                    for j in range(c1):
                        dato=float(input("Ingrese el valor de ["+str(i+1)+"]["+str(j+1)+"]: "))
                        A[i][j]=dato
                print("Matriz B")
                for i in range(f2):
                    for j in range(c2):
                        dato=float(input("Ingrese el valor de ["+str(i+1)+"]["+str(j+1)+"]: "))
                        B[i][j]=dato
                        C[i][j]=A[i][j]-B[i][j]
                print()
                print("Matriz A:")
                print(A)
                print("Matriz B:")
                print(B)
                print("-----RESULTADO-----")
                print(C)
                print()
                print("-----FIN DE RESTA DE MATRICES------")        
            else:
                print("----NO SE PUEDE RESTAR LAS MATRICES----")
                break

        elif opcion==int(3):
#-----------------------------------------------------------------------------------------------------------------------------------------
#--------------OPCION 3-------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------
            print("-------PRODUCTO DE UNA MATRIZ CON UN ESCALAR--------")
            f=int(input("Ingrese el numero de filas de la matriz:"))
            c=int(input("Ingrese el numero de columnas de la matriz:"))
            A=np.empty((f,c))
            C=np.empty((f,c))
            for i in range(f):
                for j in range(c):
                    A[i][j]=float(input("Ingrese el valor de A["+str(i+1)+"]["+str(j+1)+"]:"))
            e=float(input("Ingrese el escalar a multiplicar:"))
            for i in range(f):
                for j in range(c):
                    C[i][j]=A[i][j]*e
            print()
            print("LA MATRIZ:")
            print(A, "multiplicado por", e)
            print()
           
            print("RESULTADO:")
            print(C)
            print("-----------FIN DE PRODUCTO DE UNA MATRIZ CON UN ESCALAR-------")
        
        elif opcion==int(4):
#-----------------------------------------------------------------------------------------------------------------------------------------
#--------------OPCION 4-------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------

# Solicitar al usuario las dimensiones de las matrices
                print("       ------MULTIPLICACION DE MATRICES------")
                filas_a = int(input("Ingrese el número de filas de la matriz A: "))
                columnas_a = int(input("Ingrese el número de columnas de la matriz A: "))

                filas_b = int(input("Ingrese el número de filas de la matriz B: "))
                columnas_b = int(input("Ingrese el número de columnas de la matriz B: "))

# Verificar si las dimensiones son adecuadas para la multiplicación de matrices
                if columnas_a != filas_b:
                    print("No es posible multiplicar estas matrices. El número de columnas de A debe ser igual al número de filas de B.")
                else:
    # Ingresar los elementos de las matrices A y B
                    matriz_a = np.zeros((filas_a, columnas_a))
                    matriz_b = np.zeros((filas_b, columnas_b))

                    print("Ingrese los elementos de la matriz A:")
                    for i in range(filas_a):
                        for j in range(columnas_a):
                            matriz_a[i][j] = float(input(f"Elemento A[{i+1}][{j+1}]: "))

                    print("Ingrese los elementos de la matriz B:")
                    for i in range(filas_b):
                        for j in range(columnas_b):
                            matriz_b[i][j] = float(input(f"Elemento B[{i+1}][{j+1}]: "))

    # Multiplicar las matrices
                    resultado = np.dot(matriz_a, matriz_b)

    # Imprimir el resultado
                    print("Matriz A:")
                    print(matriz_a)

                    print("Matriz B:")
                    print(matriz_b)

                    print("Resultado de la multiplicación:")
                    print(resultado)

                    print()
                    print("        -------FIN DE PRODUCTO DE MATRICES-------")



        elif opcion==int(5):
#-----------------------------------------------------------------------------------------------------------------------------------------
#--------------OPCION 5-------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------
            print("             -------TRANSPUESTA DE UNA MATRIZ-------")
            m=int(input("Ingrese el numero de filas de la matriz: "))
            n=int(input("Ingrese el numero de columnas de la matriz: "))
            A=np.empty((m,n))
            T=np.empty((n,m))

            print()
            print("Ingresando los valores de la Matriz...")
            for i in range(m):
                for j in range(n):
                    dato=float(input("Ingrese el valor de A["+str(i+1)+"]["+str(j+1)+"]: "))
                    A[i][j]=dato
                    T[j][i]=dato

            print("Matriz original:")
            print()
            for i in range(m):
                for j in range(n):
                    print(A[i][j], end="  ")
                print()

            print("Matriz transpuesta:")
            print()
            for i in range(n):
                for j in range(m):
                    print(T[i][j], end="  ")
                print()
            print("---------------FIN DE TRANSPUESTA DE UNA MATRIZ------------------")




        elif opcion==int(6):
#-----------------------------------------------------------------------------------------------------------------------------------------
#--------------OPCION 6-------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------  
                print("       -------INICIO DE INVERSA DE UNA MATRIZ-------")
                    # Función para calcular la inversa de una matriz usando el método de Gauss-Jordan
                def calcular_inversa(matriz):
                        
                            matriz = np.array(matriz, dtype=float)
                            num_filas, num_columnas = matriz.shape
                            if num_filas != num_columnas:
                                return None

                            # Crear una matriz identidad del mismo tamaño
                            matriz_identidad = np.identity(num_filas)

                            # Crear una matriz aumentada con la matriz original y la matriz identidad
                            matriz_aumentada = np.hstack((matriz, matriz_identidad))

                            # Mostrar la matriz aumentada antes de aplicar Gauss-Jordan
                            print("Matriz aumentada antes de Gauss-Jordan:")
                            print(matriz_aumentada)

                            # Aplicar el método de Gauss-Jordan
                            for i in range(num_filas):
                                # Escalar la fila actual para que el elemento en la diagonal sea 1
                                diagonal_element = matriz_aumentada[i, i]
                                matriz_aumentada[i, :] /= diagonal_element

                                # Mostrar la matriz después de escalar la fila
                                print(f"\nPaso {i + 1}: Escalar fila {i + 1} para que el elemento en la diagonal sea 1")
                                print(matriz_aumentada)

                                # Eliminar otros elementos en la columna
                                for j in range(num_filas):
                                    if j != i:
                                        factor = matriz_aumentada[j, i]
                                        matriz_aumentada[j, :] -= factor * matriz_aumentada[i, :]

                                # Mostrar la matriz después de eliminar otros elementos en la columna
                                print(f"\nPaso {i + 1}: Eliminar otros elementos en la columna {i + 1}")
                                print(matriz_aumentada)

                            # La parte derecha de la matriz aumentada es la inversa de la matriz original
                            inversa = matriz_aumentada[:, num_filas:]

                            return inversa.tolist()
                        #RETORNAMOS la inversa como lista

                    # Ingresa tu matriz aquí 
                print('----------------CALCULO DE LA INVERSA DE UNA MATRIZ-----------------------')
                rango=int(input('Ingrese dimension de matriz: '))
                print('Ingrese la matriz: ')
                A= [list(map(float, input().split())) for i in range(rango)]
                    # Calcula la inversa
                inversa = calcular_inversa(A)
                    #Impresion de inversa fila por fila
                if inversa:
                        print("\nInversa de la matriz:")
                        for fila in inversa:
                            print(fila)

                print("        -------FIN DE INVERSA DE UNA MATRIZ  -------")

        elif opcion==int(7):
#-----------------------------------------------------------------------------------------------------------------------------------------
#--------------OPCION 7-------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------- 
                print("      -------INICIO DE RANGO DE UNA MATRIZ-------")
                f=int(input("Ingrese numero de filas de Matriz: "))
                c=int(input("Ingrese numero de columnas de Matriz: "))
                A=np.empty((f,c))
                for i in range(f):
                    for j in range(c):
                        dato=float(input("Ingrese el valor de ["+str(i+1)+"]["+str(j+1)+"]: "))
                        A[i][j]=dato

                # Calcula el rango de la matriz
                rango = np.linalg.matrix_rank(A)

                print("Matriz:")
                print(A)
                print("Rango de la matriz:", round(rango))
                print("      -------FIN DE RANGO DE UNA MATRIZ-------")




        elif opcion==int(8):
#-----------------------------------------------------------------------------------------------------------------------------------------
#--------------OPCION 8-------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------                  
                print("--------CALCULO DEL DETERMINANTE DE UNA MATRIZ--------")
                r=int(input("Ingrese el rango de la matriz: "))
                A=np.empty((r,r))
                for i in range(r):
                    for j in range(r):
                        dato=float(input("Ingrese el valor de A["+str(i+1)+"]["+str(j+1)+"]= "))
                        A[i][j]=dato
                determinante=np.linalg.det(A)
                print()
                print("La determinante es: ", round(determinante))

                print("      -------FIN DE CALCULO DE DETERMINANTE-------")      