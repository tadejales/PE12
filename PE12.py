def dividors(number): #deljitelji števila
    devidors_list = [] #lista deljiteljev
    for devidor in range (1, number + 1):
        if number % devidor == 0:
            devidors_list.append(devidor) #dodajanje deljitelja na listo
            if len(devidors_list) > 5:
                return devidors_list

    return False

    curent_number_list = []
    curent_number = 0
    sum_of_curent_numbers = 0

    """
    while 1:
        curent_number_list.append(curent_number) #dodajanje trenutnega števila na listo
        print (curent_number_list)
        print (devidors_list)
        if dividors(sum_of_curent_numbers) == True:
            print (curent_number)
            break
        else:
            break
        curent_number += 1
        sum_of_curent_numbers = sum_of_curent_numbers + curent_number
    """

    print(dividors(21))
