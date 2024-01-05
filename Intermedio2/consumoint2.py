import os
import anualmensualint2 as tiemp

def registrarconsumo(buscar:str, dependencias : list[str]) :
    is_dependencia = False
    factoremisionelec = 100
    factoremisiontransporte = 7.53
    isActive = True
   

    
    while isActive:
        for indice, dependencia in enumerate(dependencias):

            if buscar.upper() == dependencia[0].upper():
                is_dependencia = True
                rta = "S"

                while rta == "S":
                    os.system("cls")
                    print("QUE TIPO DE CONSUMO DESEA REGISTRAR")
                    print("   1. CONSUMO DE ELECTRICIDAD\n   2. CONSUMO DE TRANSPORTE\n   3.SALIR")

                    try:
                        claseconsumo = int(input(":) "))
                        os.system("cls")
                    except ValueError:
                        print("ERROR EN EL VALOR SUMINISTRADO")
                        os.system("cls")
                    
                    if claseconsumo == 1:
                        print("CONSUMO ELECTRICIDAD")

                        try:    
                            seleccion = int(input("DESEA DAR:\n SU CONSUMO TOTAL (1) \n POR DISPOSITIVO  (2)\n:) "))
                        except ValueError:
                            print("ERROR EN EL VALOR SUMINISTRADO")
                            os.system("cls")

                        if seleccion == 1:
                            try:
                                select = int(input("EL CONSUMO DE SU FACTURA ES MENSUAL(1) O OTRO INTERVALO DE TIEMPO(2): "))
                            except ValueError:
                                print("ERROR EN EL VALOR SUMINISTRADO")
                                os.system("cls")

                            if select == 1:

                                try:
                                    print("Emiciones CO2(ELECTRICIDAD) = CONSUMO ELECTRICIDAD X FACTOR DE EMISION ELECTRICIDAD\n ")
                                    consum = float(input("DIGITE EL VALOR DE SU CONSUMO MENSUAL: "))
                                    consumo = consum * factoremisionelec
                                    coselectricidad= ["ELECRIDICAD",[consumo]]
                                    os.system("cls")

                                    print(f"\nSU FACTOR DE CONSUMO DE CO2 ES DE: {consumo} gCO2/kWh")
                                    os.system("pause")
                                    dependencia.append(coselectricidad)
                                    print(dependencia)                               
                                except ValueError:
                                    print("Error: Ingrese un valor numérico válido.")

                            elif select == 2:
                                os.system("cls")

                                consum = tiemp.consumobimestral()

                                if consum > 0:
                                    consumo = consum * factoremisionelec
                                    print(f"SU CONSUMO EN ESTE PERIODO DE TIEMPO FUE DE {consumo} kWh\n")
                                    
                                    coselectricidad= ["ELECRIDICAD",[consumo]]
                    

                                    print(f"\nSU FACTOR DE CONSUMO DE CO2 ES DE: {consumo} gCO2/kWh")
                                    os.system("pause")
                                    dependencia.append(coselectricidad)
                                    os.system("pause")
                                else:
                                    print("NO SE ENCONTRÓ EL PERIODO DE TIEMPO")
                                    os.system("pause")
                        elif seleccion == 2:
                            
                            
                            dispositivos = []
                            isActive = True
                            while (isActive):
                                os.system("cls")
                                print ("CONSUMO POR DIPOSITIVO\n  Consumo de disposivo = Potencia del dispositivo en W x Tiempo de uso en horas/1000\n ")
                                try:
                                    potencia = float(input("DIGITE LA POTENCIA DEL DISPOSITIVO: "))
                                    tiempo = float(input("DIGITE EL NUMERO DE HORAS EN UNO (una hora y media = 1.30): "))
                                except ValueError:
                                    print("ERROR EN EL VALOR SUMINISTRADO")
                                    os.system("pause")
                                consumodispositivo =potencia * tiempo / 1000
                                dispositivos.append(consumodispositivo)
                                
                                rta = input("¿DESEA REGISTRAR OTRO DISPOSITIVO? S(si)/N(no): ").upper()
                                if rta != "S":
                                    isActive = False
                            

                            

                            consum = sum(dispositivos)
                            print("Emiciones CO2(ELECTRICIDAD) = CONSUMO ELECTRICIDAD X FACTOR DE EMISION ELECTRICIDAD\n ")
                            consumo = consum * factoremisionelec
                            coselectricidad= ["ELECRIDICAD",[consumo]]
                            print(f"\nSU FACTOR DE CONSUMO DE CO2 ES DE: {consumo} gCO2/kWh")
                            os.system("pause")
                            dependencia.append(coselectricidad)
                            print(dependencia)
                            os.system("pause")
                    

                    elif claseconsumo == 2  :
                        try:
                            select = int(input("EL CONSUMO DE SU FACTURA ES MENSUAL(1) O OTRO INTERVALO DE TIEMPO(2): "))
                        except ValueError:
                            print("NO SE RECONOCE EL DATO INGRESADO")

                        if select == 1:

                                try:
                                    os.system("cls")
                                    print("Emiciones CO2(TRANSPORTE) = KILOMETROS RECORRIDOS X FACTOR DE EMISION TRANSPORTE\n ")
                                    consum = float(input("DIGITE LOS KILOMETROS RECORRIDOS: "))
                                    consumo = consum * factoremisiontransporte
                                    cosgasolina = ["TRANSPORTE",[consumo]]
                                    

                                    print(f"\nSU FACTOR DE CONSUMO DE CO2 ES DE: {consumo} gCO2/km")
                                    os.system("pause")
                                    dependencia.append(cosgasolina) 
                                    print(dependencia)
                                    os.system("pause")                              
                                except ValueError:
                                    print("Error: Ingrese un valor numérico válido.")

                        elif select == 2:

                                consum = tiemp.consumobimestral()

                                if consum > 0:
                                    consumo = consum * factoremisiontransporte
                                    print(f"SU CONSUMO EN ESTE PERIODO DE TIEMPO FUE DE {consumo} g/km\n")
                                    cosgasolina = ['TRANSPORTE',[consumo]]
                    

                                    print(f"\nSU FACTOR DE CONSUMO DE CO2 ES DE: {consumo} gCO2/km")
                                    os.system("pause")
                                    dependencia.append(cosgasolina)
                                    print(dependencia)
                                    os.system("pause")
                                else:
                                    print("NO SE ENCONTRÓ EL PERIODO DE TIEMPO")
                    
                                    os.system("pause")
                    elif claseconsumo == 3:
                        isActive = False
                        break
            if not is_dependencia:
                print("NO SE ENCONTRÓ LA DEPENDENCIA")
                os.system("pause")
                isActive = False
                break            
                    
                    
           
    
    


                    


                