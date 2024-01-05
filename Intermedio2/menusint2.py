import os

menu = "\nMENU PRINCIPAL\n   1.Registrar dependencia\n   2.Registrar consumo por dependencia \n   3.Ver CO2 producido\n   4.Dependencia que produce mas CO2\n   5.Salir"
def menuprincipal() -> int:
    global hasError 
    hasError = True
    print (menu)
    while (hasError == True):
        try:
            hasError = False
            return int(input(":)"))
        except ValueError:
            print ("NO SE RECONOCE EL DATO INGRESADO")
            os.system ("pause")

def registrardependencia()->list:
    rta = "S"
    isActive = True
    while(isActive):
        
        dependencia = input("REGISTRE LA DEPENDENCIA: ").upper()  
        dependen = [dependencia]
        

        rta = input("¿DESEA REGISTRAR OTRA DEPENDENCIA? S(si)/N(no): ").upper() 
        if (rta != "S"):
            isActive = False
     
    return dependen




