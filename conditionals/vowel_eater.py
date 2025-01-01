def vowel_eater():
    try:
        while True:
            inp = input('Enter Word: ')
            user_word = inp.upper()
            vowel_bag = ['A', 'E', 'I', 'O', 'U']
            new_letter = []

            for element in user_word:
                if element not in vowel_bag:
                    new_letter.append(element)
            print(''.join(new_letter))

    except Exception as e:
        print(e)

vowel_eater()