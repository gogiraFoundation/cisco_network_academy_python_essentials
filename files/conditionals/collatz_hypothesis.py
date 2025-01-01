

def collatzhypothesis():
    inp = int(input('Enter Integer: '))
    count = 0

    if inp < 1:
        inp = int(input('Please Enter a natural number: '))
        return

    while inp != 1:
        print(f'The new input is: {inp}')
        if inp % 2 == 0:
            inp //= 2
        else:
            inp = 3 * inp + 1
        count += 1

    print(f'The number of steps: {count}')
    print(f'The last input is: {inp}')

collatzhypothesis()