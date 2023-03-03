'''
COP3502C Spring 2023, Lisha Zhou
lab 06 - Version Control
Donovan Porter ufid: 3156-0961
donovanporter@ufl.edu
'''

def encoder(pw):
    '''
    Takes string value of integers. Returns an encrypted string value of integers.
    '''

    password = list(pw)

    encoded = ''

    for i in password:

        i = int(i)

        i += 3

        encoded += str(i)

    return encoded


def menu():
    '''
    Displays a menu to the user, and asks for a choice.
    '''

    print('''What would you like to do?
1. Encode
2. Decode
3. Quit
''')

    choice = input()

    if int(choice) < 1 and int(choice) > 3:

        raise ValueError('Choice out of bounds.')

    return choice


def main():
    '''
    Main logic loop.
    '''

    try:

        chose = int(menu())

        # Third option is 'Quit'
        if chose == 3:

            print('Have a nice day.')

            quit()

        # First option is 'Encode'
        elif chose == 1:

            print('Please enter a password to encode:')

            passing = input()

            super_encoded = encoder(passing)

        # Waiting for your code for if choice is 'Decode'.
        elif chose == 2:



    # Restarts program if choice is out of bounds.
    except ValueError:

        print('Please enter an integer 1, 2, or 3.')

        main()

    # Restarts program.
    main()


# What's this called? A dunder?
if __name__ == '__main__':
    main()


# Congratulations if you have gotten this far.
# But, now you must die.
# My attack kitten leaves no survivors.

# /\     /\
#/  \   /  \
# (*)   (*)
#  =  M  =
#   mwrar
