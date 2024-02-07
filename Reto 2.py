# 1º Ejercicio del RETO Python

print ("Por favor introduzca los datos solicitados")
print ("-------------------------------------------")

print() # para que no salga todo seguido


# Pregunta por el número de registros a incorporar.
num_regis = int(input("Introducca el número de registros a grabar...:"))

print()
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
    else:
        print("Error en la introducción de Datos, vuelva a intentarlo por favor.")
#Para que si no ha sido válido no lo contabilice.
x= x-1