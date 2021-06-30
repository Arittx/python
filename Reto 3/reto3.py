import os
import numpy as np

def validateLatitude (latitude): 
    minLatitude = -4.227
    maxLatitude = -3.002

    if (not not latitude.strip()):
        latitude = float (latitude)

        if (latitude >= minLatitude and latitude <= maxLatitude): 
            return True
        else:
            print ("Error coordenada")
            return False
    print ("Error")
    return False 

def validateLongitude (longitude): 
    minLongitude = -70.365
    maxLongitude = -69.714 

    if (not not longitude.strip()):
        longitude = float (longitude)

        if (longitude >= minLongitude and longitude <= maxLongitude): 
            return True
        else:
            print ("Error coordenada")
            return False
    print ("Error")
    return False 

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

                registeredCoordenates = False
                homeCoordenate = np.array ([])
                workCoordenate = np.array ([])
                parkCoordenate = np.array ([])
                locationCoordenates = np.empty([3,2], dtype=float)

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

                            if not registeredCoordenates:
                            
                                #REGISTER HOME COORDENATES
                                print ("Ingresar coordenadas de hogar")
                                homeLatitude = input ("Ingresar latitud")
                                homeLatitudeValidation = validateLatitude (homeLatitude)

                                if homeLatitudeValidation: 
                                    homeLatitude = float (homeLatitude)
                                    homeCoordenate = np.append (homeCoordenate,format (homeLatitude, ".3f"))
                                else:
                                    break

                                homeLongitude = input ("Ingresar longitud")
                                homeLongitudeValidation = validateLongitude (homeLongitude)

                                if homeLongitudeValidation: 
                                    homeLongitude = float (homeLongitude)
                                    homeCoordenate = np.append (homeCoordenate, format (homeLongitude, ".3f"))
                                    locationCoordenates[0] = homeCoordenate
                                else:
                                    break

                                #REGISTER WORK COORDENATES

                                print ("Ingresar coordenadas de trabajo")
                                workLatitude = input ("Ingresar latitud")
                                workLatitudeValidation = validateLatitude (workLatitude)

                                if workLatitudeValidation: 
                                    workLatitude = float (workLatitude)
                                    workCoordenate = np.append (workCoordenate,format (workLatitude, ".3f"))
                                else:
                                    break

                                workLongitude = input ("Ingresar longitud")
                                workLongitudeValidation = validateLongitude (workLongitude)

                                if workLongitudeValidation: 
                                    workLongitude = float (workLongitude)
                                    workCoordenate = np.append (workCoordenate, format (workLongitude, ".3f"))
                                    locationCoordenates[1] = workCoordenate
                                else:
                                    break

                                #REGISTER PARK COORDENATES

                                print ("Ingresar coordenadas de parque")
                                parkLatitude = input ("Ingresar latitud")
                                parkLatitudeValidation = validateLatitude (parkLatitude)

                                if parkLatitudeValidation: 
                                    parkLatitude = float (parkLatitude)
                                    parkCoordenate = np.append (parkCoordenate,format (parkLatitude, ".3f"))
                                else:
                                    break

                                parkLongitude = input ("Ingresar longitud")
                                parkLongitudeValidation = validateLongitude (parkLongitude)
                                
                                if parkLongitudeValidation: 
                                    parkLongitude = float (parkLongitude)
                                    parkCoordenate = np.append (parkCoordenate, format (parkLongitude, ".3f"))
                                    locationCoordenates[2] = parkCoordenate
                                else:
                                    break 

                                backToMenu = True
                                registeredCoordenates = True
                            else:
                                counter = 1
                                for coordenate in locationCoordenates:
                                    latitude = coordenate [0]
                                    longitude = coordenate [1]
                                    print ("coordenada [latitud,longitud] " + str(counter) + " : ['"+ str(latitude) + "', '"+ str(longitude) + "']")
                                    counter = counter + 1

                                latitudes = locationCoordenates[:,0]
                                longitudes = locationCoordenates[:,1]
                                minLatitudeIndexes = np.where(latitudes == np.amin(latitudes))
                                minLongitudesIndexes = np.where(longitudes == np.amin(longitudes))
                                
                                minLatitudeIndex = minLatitudeIndexes[0][0]
                                minLongitudeIndex = minLongitudesIndexes[0][0]

                                print("La coordenada  " + str(minLatitudeIndex + 1) + " es la que está más al sur")
                                print("La coordenada  " + str(minLongitudeIndex + 1) + " es la que está más al occidente")
                                print("Presione 1,2 o 3 para actualizar la respectiva coordenadas")
                                selection = int(input("Presione 0 para regresar al menu"))
                                
                                if selection == 0 or selection == 1 or selection == 2 or selection == 3:
                                    if selection != 0 :
                                        index = selection - 1

                                        newCoordenate = np.array ([])
                                        newLatitude = input ("Ingresar latitud")
                                        newLatitudeValidation = validateLatitude (newLatitude)

                                        if newLatitudeValidation: 
                                            newLatitude = float (newLatitude)
                                            newCoordenate = np.append (newCoordenate,format (newLatitude, ".3f"))
                                        
                                        else:
                                            break

                                        newLongitude = input ("Ingresar longitud")
                                        newLongitudeValidation = validateLongitude (newLongitude)
                                
                                        if newLongitudeValidation: 
                                            newLongitude = float (newLongitude)
                                            newCoordenate = np.append (newCoordenate, format (newLongitude, ".3f"))
                                            locationCoordenates[index] = newCoordenate
                                        else:
                                            break 
                                        backToMenu = True
                                    else:
                                        backToMenu = True
                                else:
                                    print ("Error actualización")

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

