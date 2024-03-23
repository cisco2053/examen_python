#solicira al usuario que ingrese 10 numeros.
#entrada = int(input("Ingrese cuantos numeros va a ingresar: "))
#a=0
#for i in range( 1, entrada+1 ):
 # num = int (input(f"Ingrese el numero {i}: "))
  #if num > a:
   # a = num 
#print(num)


def promedio():   
    valores = []   
    while True:
        valor = int(input("validar un promedio: "))
        if valor ==  0:
            break 
        else:
            valores.append(valor)           
    average = valores / len(valores)        
    print("promedio es:",average)   
    print(valores) 



