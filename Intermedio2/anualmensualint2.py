import os

def consumobimestral() -> float:
    isBimestral = True
    while isBimestral:
        os.system("cls")
        try:
            seleccion = int(input("DIGITE EL NUMERO DE MESES EN EL PERIODO DE SU FACTURA: "))
            print (" ")
            consumo = float(input("DIGITE EL VALOR A REGISTRAR EN ESTE PERIODO DE TIEMPO: "))
            
            consumomensual = consumo/seleccion
            return consumomensual
        except ValueError:
            print("ERROR EN EL VALOR SUMINISTRADO")
            os.system("pause")
    

