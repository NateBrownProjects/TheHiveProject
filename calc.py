import math
import hive
def calculator(): 
    print('Loading up the H.I.V.E Calculator...')
    talk('Loading up the HIVE Calculator...')
    print('H.I.V.E Calculator Successfully loaded!')
    talk('HIVE Calculator Successfully loaded!')
    operation = input('''
            Please type in the math operation you would like to complete:
            + for addition
            - for subtraction
            * for multiplication
            / for division
            ''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)


    else:
        run_hive()
