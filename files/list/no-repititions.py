

def norepetitions(sorted_list=[]):
    '''
    function to check if elements in a list appears more than once 
    '''

    new_list = []
    for element in sorted_list:
        if element in new_list[:]:
            continue
        else:
            new_list.append(element)
    return new_list




my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

unique_list = norepetitions(sorted_list=my_list)

for element in unique_list:
    print(f"The list with unique elements only: {element}")
print(my_list)
print(unique_list)

    