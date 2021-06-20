#Mensaje de bienvenida
print ("Bienvenido al sistema de ubicación para zonas públicas WIFI")

#Usuario y contraseña
userPreset = 51606
passwordPreset =  60615

user = int (input ("Nombre de Usuario:\n"))

if user == userPreset:    
    password = int (input ("Contraseña:\n"))
    if password == passwordPreset:
        #Se toma dinamicamente la longitud del usuario para calcular el indice de inicio y fin para obtener los terminos requeridos
        codeLentgh = len(str(userPreset))
        startIndex = codeLentgh - 3
        lastIndex = codeLentgh
        #Se obtienen los dos terminos requeridos
        firstTerm = int(str(userPreset)[startIndex:lastIndex])
        secondTerm = int(str(userPreset)[codeLentgh - 2])
        #Se hacen los calculos de 3 ecuaciones aritmeticas que el resultado sea igual al segundo termino
        firstEq = ((5+1)-6)*6
        secondEq = (6-6)%(5+1)
        thirdEq = (5-1)*(6-6)
        #Se valida que los resultados sean igual al segundo termino
        if secondTerm == firstEq and secondTerm == secondEq and secondTerm == thirdEq:
            expectedValue = firstTerm + secondTerm 
            result = int (input (str (firstTerm) + " + " + str(secondTerm) + " = "))
            if result == expectedValue: 
                print ("Sesión Iniciada")
            else:
                print ("Error")
    else:
        print   ("Error") 
else:
    print ("Error")
