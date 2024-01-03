import os
n = 0
par = 0
menor10 = 0
entre20 = 0
mas100 = 0
impar = 0
numerospar = []
numerosimpar = []
isActive = True
while (isActive):
    try:
        os.system("cls")
        num = int(input("INGRESE UN NUMERO: "))
        if (num >= 0):
            n +=1
            if (num % 2 == 0):
                par += 1
                numerospar.append(num)
            else:
                numerosimpar.append(num)
                impar += 1
            
            if ( num <= 10):
                menor10 +=1
            elif(num >= 20 and num <= 50):
                entre20 +=1
            elif(num >= 100):
                mas100 += 1

            
        else:
            print ("INGRESO UN NUMERO NEGATIVO")
            os.system("pause")
            isActive = False
    except ValueError:
        print ("ERROR EN LA DIGITACION DE DATOS")

os.system("cls")

print(f"TOTAL DE NUMEROS INGRESADOS       : {len(numerospar) + len(numerosimpar)}")
print(f"TOTAL DE NUMEROS PARES INGRESADOS : {len(numerospar)}")
print(f"PROMEDIO DE NUMEROS PARES         : {sum(numerospar)/len(numerospar)}")
print(f"PROMEDIO DE NUMEROS IMPARES       : {sum(numerosimpar)/len(numerosimpar)}")
print(f"NUMEROS MENORES DE 10             : {menor10}")
print(f"NUMEROS ENTRE 20 Y 50             : {entre20}" )
print(f"MAYORES A 100                     : {mas100}")

        




