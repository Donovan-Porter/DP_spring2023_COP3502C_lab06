'''
COP3502C Spring 2023, Lisha Zhou
lab 06 - Version Control
Donovan Porter ufid: 3156-0961
donovanporter@ufl.edu
'''
super_encoded = ''
super_decoded = ''
passing = ''


def encoder(pw):
    '''
    Takes string value of integers. Returns an encrypted string value of integers.
    '''

    password = list(pw)

    encoded = ''

    for i in password:

        if i == '7' or i == '8' or i == '9':

            i = int(i)

            i = i + 3 - 10

        else:

            i = int(i)

            i += 3


        encoded += str(i)

    return encoded

# This function decodes a previously encoded password
def decoder(encoded):

    decoded = ''

    encoded = str(encoded)

    for i in encoded:

        i = int(i)

        if i == 2 or i == 1 or i == 0:

            i = i + 10

        i -= 3

        decoded += str(i)

    return decoded

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
    global super_encoded
    global super_decoded
    global passing

    try:


        chose = int(menu())

        # Third option is 'Quit'
        if chose == 3:

            quit()

        # First option is 'Encode'
        elif chose == 1:

            print('Please enter your password to encode: ')

            passing = input()

            print('Your password has been encoded and stored!')

        # I put in the code for this part of main!! I tried to match your formatting as best I could.
        elif chose == 2:

            super_encoded = encoder(passing)

            super_decoded = decoder(super_encoded)

            print(f'The encoded password is {super_encoded}, and the original password is {super_decoded}.\n')

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

# You fool! I have created an equally powerful being.
# Meet the smiley face which is very good at beating up kittens!!
# While they fight I shall sneak away unscathed.

#    _________
#   / (@)  (@)\
#  |  \______/ |
#   \_________/
# *Grins*