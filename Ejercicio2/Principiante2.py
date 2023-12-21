import os
isActive = True
estudiantes= []
NumEstudiantes = 0
if (NumEstudiantes <=20):
    while (isActive):
        try:
            nombre = input("Ingrese su nombre: ")
            edad= int(input("Ingrese su edad: "))
            os.system("cls")
            imc = float(input(f"ingrese su peso en kg: "))/float(input(f"ingrese su altura en m: "))**2
            print(f"Su Indice de Masa Corporal(IMC) es de: {imc}")
            if (imc > 18.5) and (imc < 24.9):
                ClasificacionIMC = "NORMAL" 
                print("Su nivel de IMC esta en normal")
            elif ((imc > 25 ) and (imc < 29.9)):
                ClasificacionIMC = "SOBREPESO"
                print("Su nivel de IMC esta en sobrepeso")
            elif ((imc > 30) and (imc < 34.9)):
                ClasificacionIMC = "OBESIDAD I"
                print("Su nivel de IMC esta en obesidad I")
            elif ((imc > 35) and (imc < 39.9)):
                ClasificacionIMC = "OBESIDAD II"
                print("Su nivel de IMC esta en obesidad II")
            elif (imc > 40):
                ClasificacionIMC = "OBESISDAD III" 
                print("Su nivel de IMC esta en obesidad III")
            os.system ("pause")
            NumEstudiantes += 1
            estudiantes.append(ClasificacionIMC)
            Seleccion = input("¿Desea registrar otra persona? S(si) o N(no)").upper()
            print(estudiantes)   
            if (Seleccion == "S"):
                isActive = True
            elif (Seleccion == "N"):
                isActive = False
        
        except ValueError:
            print("Error en la digitacion de los datos")
            isActive = True

     


       
