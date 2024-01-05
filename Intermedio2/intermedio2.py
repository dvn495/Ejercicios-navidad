import os
import menusint2 as menu
import consumoint2 as consumo
import co2int2 as co2
isActive = True
dependencias = []
opmenu = 0


while isActive:
    os.system("cls")
    opmenu = menu.menuprincipal()

    if opmenu == 1:
        os.system("cls")
        dependencias.append(menu.registrardependencia())
    elif opmenu == 2:
        os.system("cls")
        buscar = str(input("INGRESE EL NOMBRE DE LA DEPENDENCIA: "))
        consumo.registrarconsumo(buscar, dependencias)
    elif opmenu == 3:
        os.system("cls")
        buscar = str(input("INGRESE EL NOMBRE DE LA DEPENDENCIA A BUSCAR: "))
        co2.VerCo2(buscar, dependencias)
    elif opmenu == 4:
        print (dependencias)
        os.system("pause")

