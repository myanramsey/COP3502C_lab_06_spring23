'''
Mya Ramsey
Lael Thomas
lab 06
'''

def encode(phrase):
    new_phrase = ""
    for num in phrase:
        num = int(num)
        num += 3
        num = str(num)
        new_phrase += num

    return new_phrase

def decode(phrase):
    decoded_password = ""
    for element in phrase:
        new_element = int(element)
        decoded_element = new_element - 3
        new_decoded_element = str(decoded_element)
        decoded_password += new_decoded_element
    return decoded_password

def main():
    # looping menu
    option = '1'
    phrase = ''
    while option != '0':
        # print menu
        print('0. Exit')
        print('1. Enter a new phrase')
        print('2. Print encoded phrase')
        print('3. Print decoded phrase')
        option = input('Enter an option: ')

        if option == '1':
            phrase = input('Enter your phrase: ')
        elif option == '2':
            print('Encoded phrase is', encode(phrase))
        elif option == '3':
            print('Decoded phrase is', decode(phrase))


main()