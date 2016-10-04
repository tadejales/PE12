def dividors(number): #deljitelji števila
    devidors_list = [] #lista deljiteljev
    for devidor in range (1, number + 1):
        if number % devidor == 0:
            devidors_list.append(devidor) #dodajanje deljitelja na listo
            if len(devidors_list) > 5:
                return devidors_list

    return False
