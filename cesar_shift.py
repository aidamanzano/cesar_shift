
def print_ascii_table():
    """Function to print ASCII characters. Not used, not necessary atm."""
    for i in range(0, 128):
        print(chr(i), end = ' ')
        if (i - 1) % 10 == 0:
            print()
    print()
#print('List of valid encryption characters: ')                    
#print_ascii_table()

def is_unicode(input):
    """Checks if all user inputs are valid Unicode characters, otherwise raises error."""
    for char in input:
        try:
            ord(char)
            return True
        except UnicodeDecodeError:
            print('You entered an invalid character: ', char)
            return False


user_input = str(input('enter your string message: '))

#-------------------------------------------------------------------
"""Using Unicode Encoding, which aims to encode all possible characters.
    There are a total of 149,813 characters, hence the modulo 149813 operation."""

"""Key needs to be shared, and an integer. Input space for the plaintext is any
Unicode character, you can even try it with emojis! """

def cesar_shift_enc(input:str, key:int) -> list:
    
    string = ''
    for char in input:
        encrypted_char = ord(char) + key
        encrypted_char = encrypted_char % 149813
        string += chr(encrypted_char)
    
    return string
    
def cesar_shift_dec(encrypted_input:str, key:int) -> int:
    plaintext = ''
    for enc_char in encrypted_input:
        enc_char = ord(enc_char)
        dec_char = enc_char - key
        dec_char = dec_char % 149813
        string = chr(dec_char)
        plaintext += string

    return plaintext

if is_unicode(user_input) is True:
    encrypted_input = cesar_shift_enc(user_input, 149816)
    print('encryption: ', encrypted_input)

    plaintext = cesar_shift_dec(encrypted_input, 3)
    print('decryption: ', plaintext)
        

