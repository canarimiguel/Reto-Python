# 1º Ejercicio del RETO Python

print ("Por favor introduzca los datos solicitados")
print ("-------------------------------------------")

print() # para que no salga todo seguido


# Pregunta por el número de registros a incorporar.
num_regis = int(input("Introducca el número de registros a grabar...:"))

print()
nombre =""
apellido =""
telefono = ""
mail = ""

my_lis = []   # Creamos una lista para que almacene los registros
ide = 1 # Base de registro que deseamos poner a los registros como identificadores.
x = 1
while x <= (num_regis):
    print()
    print ("Este es el ", x , "registro introducido")
  
    print ()
    nombre = input("Nombre .............: ")
    if len(nombre) > 4 and len(nombre) < 50:
        apellidos = input("Apellidos...........: ")
    
        
        if len(apellidos) > 4 and len(apellidos) < 50 :
            telefono = int(input("Teléfono............: "))
     
            
            if len(str(telefono)) == 10 :
                mail = input("Correo electrónico..: ")
           
                
                if len(mail) > 4 and len(mail) < 50 :
                    x = x +1
                    print() # para que no salga todo seguido
                    print ("Hola" + " " + nombre + " " + apellidos + ", " + "en breve recibirás un correo en" + " " + mail)
                    #Creamos un identificador numerico por cada registro
                    
                    # como es positvo el registro, lo mandamos a guardar al final
                    my_lis.append(ide)
                    my_lis.append(nombre)
                    my_lis.append(apellidos)
                    my_lis.append(telefono)
                    my_lis.append(mail)
                    ide +=1  # Aumenta el número de identificación que le hemos creado
                   
    else:
        print("Error en la introducción de datos..RECUERDE verificar el número de caractere introducidos")
        print ("                    * * * *  Vuelva a intentarlo por favor  * * * *                     ")
    
#Para que si no ha sido válido no lo contabilice.
x= x-1

# Le preguntamos si dese visualizar los registros
pregunta_impresion = input("\nDesea que le mostremos todos los registros introducidos ..(si/no)...:")
if pregunta_impresion == "si" or pregunta_impresion == "no":
    if pregunta_impresion == "si":
        print ("\nLos registros acumulados en la actualidad, son los siguientes")
        print ("--------------------------------------------------------------.")
        print (my_lis)
    else:
        if pregunta_impresion == "no":
            print ("\nNo se mostrarán los registro, tal y como nos ha pedido.")
            print ("      *** Gracias por usar nuestro programa ***")
       
else:
    print ("Error en la introducción de datos. Debe teclaer si o no en minúscula")
    