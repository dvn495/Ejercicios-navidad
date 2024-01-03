import os


def informederiesgo (item : list, listaciudades : list, promedioriesgo : list):
    nombre_ciudad = item[0]
    lista_sismos = item[1]
    

    if len(lista_sismos) == 5:
        riesgo = sum(lista_sismos) / len(lista_sismos)
        promedioriesgo.append(riesgo)
        print(f"El riesgo en {nombre_ciudad} es de un promedio de {riesgo}")
    else:
        print(f"LA CANTIDAD DE DATOS DE SISMOS EN {nombre_ciudad} ESTÁ INCOMPLETA\n(Recuerde que debe tener registrados 5 sismos)")
    

    os.system("pause")    
    