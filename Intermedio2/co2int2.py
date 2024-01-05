import os

def VerCo2(buscar:str ,dependencias:list):
    rta = "S"
    while (rta == "S"):
        for i in dependencias:
            if buscar.upper() == i[0].upper():
                for item in i:
                    if item[0] == "TRANSPORTE":
                        print(F"LAS EMICIONES DE CO2 DE TRANSPORTE SON: {item[1]}")
                    if item[0] == "ELECRIDICAD":
                        print(F"LAS EMICIONES DE CO2 DE ELECTRICIDAD SON: {item[1]}")
                os.system("pause") 
                rta = input("DESEA VER OTRA DEPENDENCIA S(si)/N(no)").upper()      

                    



                

           

           
    
    
