

def printlog(result=None):
    print(f'Your Personal Income Tax is: {result} thalers')
    




def tax_calculator(tax=None, income=None):

    try:
        if income <= 85528:
            tax = income * 0.18 - 556.02        
        else:
            surplus = income - 85528
            tax = 14839.02 + surplus * 0.32
        
        #if tax is less than 0, set it to 0
        if tax < 0:
            tax = 0
        
        # round tax to the nearest full thalers
        tax = round(tax, 0)
        printlog(tax)
    
    except Exception as e:
        print(e)


list = [100000, 30000, 1000, 0, 834562, 85528, 86000]

for item in list:
    tax_calculator(tax=None, income=float(item))