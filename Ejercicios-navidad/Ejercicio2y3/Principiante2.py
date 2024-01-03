import os
isActive = True
estudiantes= []
NumEstudiantes = 0
PesoNormal = 0
Sobrepeso = 0
ObesidadI= 0
ObesisdadII =0
ObesidadIII= 0
while (isActive):
    while(NumEstudiantes <= 20):
        try:
            os.system ("cls")
            nombre = input("Ingrese su nombre: ")
            edad= int(input("Ingrese su edad: "))
            os.system("cls")
            imc = float(input(f"ingrese su peso en kg: "))/float(input(f"ingrese su altura en m: "))**2
            print(f"Su Indice de Masa Corporal(IMC) es de: {imc}")
            if (imc > 18.5) and (imc < 24.9):
                ClasificacionIMC = str("NORMAL") 
                print("Su nivel de IMC esta en normal")
            elif ((imc > 25 ) and (imc < 29.9)):
                ClasificacionIMC = str("SOBREPESO")
                print("Su nivel de IMC esta en sobrepeso")
            elif ((imc > 30) and (imc < 34.9)):
                ClasificacionIMC = str("OBESIDAD I")
                print("Su nivel de IMC esta en obesidad I")
            elif ((imc > 35) and (imc < 39.9)):
                ClasificacionIMC = str("OBESIDAD II")
                print("Su nivel de IMC esta en obesidad II")
            elif (imc > 40):
                ClasificacionIMC = str("OBESISDAD III" )
                print("Su nivel de IMC esta en obesidad III")

            

            NumEstudiantes += 1
            estudiantes.append(ClasificacionIMC)
            Seleccion = input("¿Desea registrar otra persona? (S) o pasar a ver el conteo (N): ").upper()
            if Seleccion == "N":
               break      

            

        except ValueError:
            print("Error en la digitacion de los datos")
            imcActive = True
    

    for item in estudiantes:
              if (item == "NORMAL"):
                PesoNormal +=1
              elif (item == "SOBREPESO"):
                Sobrepeso +=1
              elif (item == "OBESIDAD I"):
                ObesidadI +=1
              elif(item == "OBESIDAD II"):
                ObesisdadII +=1
              elif(item == "OBESIDAD III"):
                ObesidadIII +=1   
          
    print (f"Los estudiantes con un IMC en normal: {PesoNormal}")
    print (f"Los estudiantes con un IMC en sobrepeso: {Sobrepeso}")
    print (f"Los estudiantes con un IMC en obesidad I {ObesidadI}")
    print (f"Los estudiantes con un IMC en obesidad II {ObesisdadII}")
    print (f"Los estudiantes con un IMC en obesidad III {ObesidadIII}")
    Seleccion = input ("Desesa ingresar mas datos? S(si) o N(no)")
    if (Seleccion == "S"):
        isActive = True
    elif (Seleccion == "N"):
        isActive = False

     


       
