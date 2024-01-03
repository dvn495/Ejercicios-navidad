import os
menu = "1. Registrar ciudad\n2. Registrar sismos\n3. Buscar sismos por ciudad\n4. Informe de riego\n5. Salir"
hasError = True
def menuprincipal() -> int:
    global hasError
    hasError = True
    print(menu)
    while (hasError == True):
        try:
            hasError = False
            return int(input(":)"))
        except ValueError:
            print ("Error en el dato ingresado")
            hasError = True

def añadirsismo(buscarcity :str, ciudades : list  ):
    isNumsismos = True

    isciudadencontrada = False
    for item in ciudades:
        if buscarcity in item:
            indice = ciudades.index(item)
            rta = "S"
            while (rta == "S"):
                os.system("cls")
                numsismos = len(ciudades[indice][1])
                if(numsismos >= 5):
                    print("SE COMPLETO EL NUMERO DE SISMOS A REGISTRAR POR CIUDAD")
                    rta = "F"
                else:
                    try:

                        sismo= float(input("INGRESE EL NIVEL DEL SISMO: "))
                        ciudades[indice][1].append(sismo)
                    except ValueError:
                        print ("EL VALOR NO ES VALIDO")
                    
                    rta= input("DESEA INGRESAR OTRO SISMO S(si)/N(no): ").upper() 
            isciudadencontrada =True
            break
    if not isciudadencontrada:
        print("NO SE ENCONTRÓ LA CIUDAD")

    os.system("pause") 