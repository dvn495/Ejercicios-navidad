import os
import anualmensualint2 as tiempo
def registrarconsumo(dependencias : list, buscar: str):
    isdependencia = False
    factoremisionelec = 100
    for dependencia in dependencias:
        if buscar in dependencia[0].upper():
            indice = dependencias.index(dependencia)
            rta = "S"
            while (rta == "S"):
                os.system("cls")
                print ("QUE TIPO DE CONSUMO DESEA REGISTRAR")
                print ("   1. CONSUMO DE ELECTRICIDAD\n   2.CONSUMO DE TRANSPORTE")
                claseconsumo = int(input(":) "))
                os.system("cls")
                if (claseconsumo == 1):
                    print ("CONSUMO ELECTRICIDAD")
                    seleccion = int(input("DESEA DAR SU CONSUMO TOTAL(presente el en recibo)-SELECCIONE 1\n \nDESEA DAR SU CONSUMO POR DISPOSITIVO -SELECIONE\n:) "))
                    if seleccion == 1:
                        select = int(input("EL CONSUMO DE SU FACTURA ES MENSUAL(1) O OTRO INTERVALO DE TIEMPO(2):) "))
                        if select == 1:
                            print ("Emiciones CO2(ELECTRICIDAD) = CONSUMO ELECTRICIDAD X FACTOR DE EMISION ELECTRICIDAD")
                            consum = float(input("DIGITE EL VALOR DE SU CONSUMO MENSUAL\n:)"))
                            consumo = consum*factoremisionelec
                            cos=["Electricidad: ",consumo]
                            
                            print (f"SU FACTOR DE CONSUMO DE CO2 ES DE: {consumo}")
                            os.system("pause")
                            dependencias[indice][1].append(cos)
                        elif select == 2:
                            consumo = tiempo.consumobimestral()
                            print (consumo)

                    


                