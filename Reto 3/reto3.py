import os
import numpy as np
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
                
                cantErrors = 0
                isError = False
                backToMenu = False
                startedMenu = False
                reorderMenu = False
                cleanConsole = False
                selectedFavorite = 0 

                while (startedMenu == False or isError == True or reorderMenu == True or backToMenu == True) and cantErrors <3:
                    backToMenu = False
                    optionsList = [
                        "Cambiar contraseña", 
                        "Ingresar coordenadas actuales",
                        "Ubicar zona wifi mas cercana",
                        "Guardar archivos con ubicacion cercana",
                        "Actualizar registros de zonas wifi desde archivo"
                    ]

                    if cleanConsole == True:
                        command = 'clear'
                        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
                            command = 'cls'
                        os.system(command)

                    if reorderMenu == True:
                        reorderMenu = False
                        selectedOption = optionsList[selectedFavorite - 1]

                        optionsList.remove(selectedOption)
                        optionsList.insert(0,selectedOption)


                    initialCounter = 0 

                    for option in optionsList:
                        print (str (initialCounter +1) + " " + option)
                        initialCounter += 1

                    print ("6. Elegir opcion de menu favorita")
                    print ("7. Cerrar sesion")

                    option = int(input("Elija una opcion"))
                    if option >= 1 and option <=7:

                        if option == 7:
                            print ("Hasta pronto")

                        if option == 6: 
                            favoriteOption = int(input ("Seleccione opcion favorita"))

                            if favoriteOption >= 1 and favoriteOption <= 5:
                                answer1 = int (input ("Redondo soy y es cosa anunciada que a la derecha algo valgo, pero a la izquierda nada"))
                                if answer1 == 0:
                                    isError = False
                                    answer2 = int (input ("Si le sumas su hermano gemelo al tres en seguida sabras que numero es"))
                                    if answer2 == 6:
                                        isError = False
                                        reorderMenu = True
                                        cleanConsole = True
                                        selectedFavorite = favoriteOption
                                    else:
                                        print ("Error")
                                        isError = True
                                else: 
                                    print("Error")
                                    isError = True
                            else:
                                print ("Error")
                        if option == 5:
                            print ("Usted ha elegido la opción 5")

                        if option == 4:
                            print ("Usted ha elegido la opción 4")
                        
                        if option == 3:
                            print ("Usted ha elegido la opción 3")

                        if option == 2:
                            print ("Usted ha elegido la opción 2")

                        if option == 1:

                            print ("Usted ha elegido la opción 1")
                            currentPassword = int (input ("Ingresar contraseña actual"))

                            if currentPassword == passwordPreset:
                                newPassword = int (input ("Ingresar contraseña nueva"))

                                if newPassword != passwordPreset:
                                    passwordPreset = newPassword
                                    backToMenu = True
                                else:
                                    print ("Error")
                            else:
                                print ("Error")
                    else:
                        print ("Error")
                        isError = True
                        cantErrors += 1
                    startedMenu = True
            else:
                print ("Error")
    else:
        print   ("Error") 
else:
    print ("Error")