import os
SumActive = True
while (SumActive):
    try:
        os.system ("cls")
        num1 =int(input("Digite el numero 1: "))
        num2 =int(input("Digite el numero 2: "))
        num3 =int(input("Digite el numero 3: "))

        if (num1 >= 0) and (num2 >= 0) and (num3 >= 0):
            print (f"la suma de los numeros es {num1 + num2 + num3}")
            Seleccion = input("¿Desea realizar otra operacion? S(si) o N(no)").upper()
            if (Seleccion == "S"):
                SumActive = True
            elif (Seleccion == "N"):
                SumActive = False
        else:
             print ("Recuerde que debe ser un entero positivo")
             SumActive = True
             os.system ("pause")
    
    except ValueError:
        print ("Recuerde que debe ser un entero positivo")
        os.system ("pause")
        SumActive = True
        