
#temps = [[0.0 for h in range(24)] for d in range(31)]
temps_list = [[0.0 for h in range(24)] for d in range(31)]
total = 0.0

def average_tempreture(temps_list, total):
    """
    determine the monthly average noon temperature. 
    Add up all 31 readings recorded at noon and divide the sum by 31. 
    You can assume that the midnight temperature is stored first.    
    """
    

    for day in temps_list:
        total += day[11]
        average = total / 31
        print("Average temperature at noon:", average)
    
    return average


average_tempreture_per_month = average_tempreture(temps_list, total)


def highest_temp(temps_list):
    highest = -100.0
    for day in temps_list:
        for temps_list in day:
            if temps_list > highest:
                highest = temps_list
                print("The highest temperature was:", highest)




highest_tempreture_per_month = highest_temp(temps_list)