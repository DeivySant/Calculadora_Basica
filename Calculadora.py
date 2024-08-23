nombre = input("Por favor dame tu nombre : ")
while True :
    print("CALCULADORA DIGITAL XD ")
    print("------Opciones------- : ")
    print("------1. SUMA-------- ")
    print("------2. RESTA------- ")
    print("--3. MULTIPLICACION-- ")
    print("-----4. DIVISION----- ")
    print("- PARA CERRAR ESCRIBA 'SALIR'-")

    opci = input(f"Cual es tu opcion {nombre} : ").lower()
   
    if opci not in ["1","2","3","4","salir"]:
        print(f"--------------------------- \n!!!!!!!!!!{opci} NO EXISTE ¡¡¡¡¡¡¡¡¡¡¡ \nPor favor selecciona una opcion diferente :)\n------------------------------------------- ")

    elif opci == "1":
        print("---------------------\n------SUMA O RESTA ------\n----------------")

        while True:
            try :
                entrada1 = input("Por favor ingresa un valor numerico : ")
                num1 = float(entrada1)
                break
            except ValueError:
                print(f"! ERROR ¡ {entrada1} no es un valor numerico :( ")
        while True:
            try :
                entrada2 = input("Por favor ingresa tu segundo valor numerico : ")
                num2 = float(entrada2)
                break
            except ValueError:
                print(f"! ERROR ¡ {entrada2} no es un valor numerico, por favor selecciona otro : ") 

        suma = num1 + num2
        print("------------------------------------")
        print(f"[{num1}] + [{num2}] = [{suma}]")
        print("------------------------------------")
        print (f"La suma de sus numeros es : {suma}")


    elif opci == "2":
        print("---------------------\n------RESTA------\n----------------")
        
        while True:
            try :
                entrada1 = input("Por favor ingresa un valor numerico : ")
                num1 = float(entrada1)
                break
            except ValueError:
                print(f"! ERROR ¡ {entrada1} no es un valor numerico :( ")
        while True:
            try :
                entrada2 = input("Por favor ingresa tu segundo valor numerico : ")
                num2 = float(entrada2)
                break
            except ValueError:
                print(f"! ERROR ¡ {entrada2} no es un valor numerico, por favor selecciona otro : ")

        resta = num1 - num2
        print("------------------------------------")
        print(f"[{num1}] - [{num2}] = [{resta}]")
        print("------------------------------------")
        print (f"La resta de sus numeros es : {resta}")

    elif opci == "3" :
        print("---------------------\n------MULTIPLICACION------\n----------------")
        
        while True:
            try :
                entrada1 = input("Por favor ingresa un valor numerico : ")
                num1 = float(entrada1)
                break
            except ValueError:
                print(f"! ERROR ¡ {entrada1} no es un valor numerico :( ")
        while True:
            try :
                entrada2 = input("Por favor ingresa tu segundo valor numerico : ")
                num2 = float(entrada2)
                break
            except ValueError:
                print(f"! ERROR ¡ {entrada2} no es un valor numerico, por favor selecciona otro : ")

        mult = num1 * num2
        print("------------------------------------")
        print(f"[{num1}] * [{num2}] = [{mult}]")
        print("------------------------------------")
        print (f"La multiplicacion de sus numeros es : {mult}")

    elif opci == "4" :
        print("---------------------\n------DIVISION------\n----------------")
        
        while True:
            try :
                entrada1 = input("Por favor ingresa un valor numerico : ")
                num1 = float(entrada1)
                break
            except ValueError:
                print(f"! ERROR ¡ {entrada1} no es un valor numerico :( ")
        while True:
            try :
                entrada2 = input("Por favor ingresa tu segundo valor numerico : ")
                num2 = float(entrada2)
                break
            except ValueError:
                print(f"! ERROR ¡ {entrada2} no es un valor numerico, por favor selecciona otro : ")

        try:
            resultado = num1/num2
            print("------------------------------------")
            print(f"[{num1}] / [{num2}] = [{resultado}]")
            print("------------------------------------")
            print (f"La multiplicacion de sus numeros es : {resultado}")
        except ZeroDivisionError:
            print("¡ ERROR ! No se puede dividir por cero (0) ")
        
    elif opci == "salir":
        break
       
    
print(f"¡Que tengas buen dia {nombre}!")