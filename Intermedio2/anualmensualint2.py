import os

def consumobimestral() -> float:
    seleccion = int(input("DIGITE EL NUMERO DE MESES EN EL PERIODO DE SU FACTURA: "))
    consumo = float(input("DIGITE EL VALOR DE SU CONSUMO EN ESTE PERIODO DE TIEMPO: "))
    consumomensual = consumo/seleccion
    return consumomensual

