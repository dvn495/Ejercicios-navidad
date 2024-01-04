import os
import menusint2 as menu
import consumoint2 as consumo

isActive = True
dependencias = []
opmenu = 0

while isActive:
    os.system("cls")
    opmenu = menu.menuprincipal()

    if opmenu == 1:
        os.system("cls")
        dependencias.append(menu.registrardependencia())

    if opmenu == 2:
        os.system("cls")
        buscar = input("INGRESE EL NOMBRE DE LA DEPENDENCIA: ")
        consumo.registrarconsumo(buscar, dependencias)

