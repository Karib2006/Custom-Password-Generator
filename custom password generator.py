import random

alphabets ='qwertyuiopasdfghjklzxcvbnm'
signs = ';:-_+[{]}\|.><,'
number = '1234567890'

while True:
    length = False
    command= input('Write Password Type (type help for commands)>> ')

    if command == 'help':
        print('number - only numerical password \' alphabet - for only word password \' mixed - for mixed password \' exit - to end program')

    elif command == 'number':
        length = int(input('Length of your password >> '))
        f_number = random.choices(number, k= length)
        final_list = f_number

        random.shuffle(final_list)


        def converttostring(final_list):
            pas = ''
            return (pas.join(final_list))


        final_pas = converttostring(final_list)

        print(f"Your Password Is {final_pas}")
    elif command == 'alphabet':
        length = int(input('Length of your password >> '))
        f_alphabet = random.choices(alphabets,k= length)
        final_list = f_alphabet

        random.shuffle(final_list)


        def converttostring(final_list):
            pas = ''
            return (pas.join(final_list))

        final_pas = converttostring(final_list)
        print(f"Your Password is {final_pas}")


    elif command == 'mixed':
        unique = int(input('Number of Unique Characters in password >> '))
        num = int(input('Number of Alphabets in password >> '))
        alp = int(input('Number of numbers in password >> '))
        f_signs = random.choices(signs, k= unique)
        f_alphabet = random.choices(alphabets, k= alp)
        f_number = random.choices(number, k= num)

        final_list = f_number + f_signs + f_alphabet

        random.shuffle(final_list)


        def converttostring(final_list):
            pas = ''
            return (pas.join(final_list))


        final_pas = converttostring(final_list)
        print(f'Your Password is {final_pas}')

    elif command == 'exit':
        break

    else:
        print('Wrong command type help to see all commands')


































