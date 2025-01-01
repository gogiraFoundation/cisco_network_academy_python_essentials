def printlog(result=None):
    if result == 3:
        print(f'You have {result} attempts left, tread lightly.')
    elif result == 2:
        print(f'You have {result} attempts left, choose wisely.')
    elif result == 1:
        print(f'You have {result} attempt left, make it count.')
    else:
        print(f'You have {result}, forever loop.')

def guess_number_games(secretNumber=None):
    count = 3
    secret_number = 777

    while count > 0:
        print(
            """
            +================================+
            | Welcome to my game, muggle!    |
            | Enter an integer number        |
            | and guess what number I've     |
            | picked for you.                |
            | So, what is the secret number? |
            +================================+
            """
        )
        printlog(count)
        inp = int(input('Pick a number: '))

        if inp == secret_number:
            print("Well done, muggle! You are free now.")
            break
        else:
            count -= 1
            if count > 0:
                printlog(result=count)
            else:
                print(f'Ha ha! You\'re stuck in my loop! The secret number was {secret_number}.')

if __name__ == "__main__":
    guess_number_games(secretNumber=None)
