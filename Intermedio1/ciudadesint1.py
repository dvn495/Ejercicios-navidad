import os


def registrarciudad (conteociudades: int) -> list:
    
    if (conteociudades < 1):
        isActive = True
        ciudad = 0
        rta = "S"
        
        while (isActive):
        
            os.system("cls")
            city = input("REGISTRE LA CIUDAD: ").upper()
            if not city.isalpha():
                print ("LA CIUDAD SOLO DEBE CONTENER LETRAS")
            else:
                ciudad +=1
                citta = [city,[]]
                

            if(ciudad==5):
                print ("SE HA LLEGADO AL LIMITE DE CIUDADES A REGISTRAR")
                isActive = False   

            rta = input("¿DESEA REGISTRAR OTRA CIUDAD? S(si)/N(no)").upper()

            if (rta != "S"):
                isActive = False
        
        return citta
    else:
        print("YA SE HA ALCANZADO EL LIMITE DE CIUDADES A REGISTRAR")  
    os.system("pause")



def buscarciudad (buscarcity :str, ciudades : list  ):
   
    isciudadencontrada = False

    for item in ciudades:
        if buscarcity in item:
            print(item)
            isciudadencontrada = True
            break  

    if not isciudadencontrada:
        print("NO SE ENCONTRÓ LA CIUDAD")

    os.system("pause")
            
        
        


        


    