import os
import ciudadesint1 as ciudad
import menusint1 as menu
import sismosint1 as sismos

isActive = True
opmenu = 0
conteociudades = 0
promedioriesgo = []
listaciudades = []
while (isActive):
    os.system("cls")
    try:
        opmenu = menu.menuprincipal()
    except ValueError:
        print("ERROR EN EL DATO INGRESADO")
        os.system("pause")
    else:
        if (opmenu == 1):
            os.system ("cls")
            if (conteociudades < 1):
                listaciudades.append(ciudad.registrarciudad(conteociudades))
                print(listaciudades)
                os.system("pause")
                if (len(listaciudades) >= 5):
                   conteociudades +=2
            else:
                print("YA SE HA ALCANZADO EL LIMITE DE CIUDADES A REGISTRAR")
                os.system("pause")

        elif (opmenu == 2):
            os.system("cls")
            buscarcity = input("INGRESE LA CIUDAD PARA REGISTRAR: ").upper()
            menu.añadirsismo(buscarcity, listaciudades)
        elif (opmenu == 3):
            os.system("cls")
            buscarcity = input("INGRESE LA CIUDAD A BUSCAR: ").upper()
            ciudad.buscarciudad(buscarcity, listaciudades)
        elif (opmenu == 4):
            os.system("cls")
            isSismos = True
            while (isSismos):
                for item in listaciudades:
                    numsismos = len(item[1])
                    if (numsismos == 5):
                        sismos.informederiesgo(item, listaciudades, promedioriesgo)
                    else:
                        print(f"LA CANTIDAD DE DATOS DE SISMOS EN {item[0]} ESTAN INCOMPLETOS \n(recuerde que debe tener registrados 5 sismos)")
                        isSismos = False
                
                promedio = sum(promedioriesgo)/len(promedioriesgo)
                if (promedio < 2.5):
                    print ("EL PROMEDIO DE RIESGO DE LAS CIUDADES ES AMARILLO(sin riesgo)")
                elif (promedio >2.6 and promedio < 4.4):
                    print ("EL PROMEDIO DE RIESGO DE LAS CIUDADES ES NARANJA(riesgo medio)")
                elif (promedio > 4.5):
                    print ("EL PROMEDIO DE RIESGO DE LAS CIUDADES ES ROJO(riesgo alto)")
                os.system("pause")
                isSismos = False
        elif(opmenu == 4):
            os.system("cls")
            print("Gracias por usar nuestro sistema")
            isActive = False
        else:
            os.system("cls")
            print("Opcion invalida")
            os.system("pause")
            

          
                    





            




                




