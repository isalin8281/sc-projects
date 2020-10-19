"""
File: caesar.py
Name: Isabelle
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    User input the secret number and the string.
    The program will shift ALPHABET as cipher table and then encrypt the string.
    """
    n=int(input('Secret number: '))
    s=input("What's the ciphered string? ").upper()
    new_alphabet=alphabet(n)
    decipher(s,new_alphabet)

def alphabet(n):
    """
    Shift the ALPHABET as cipher table.
    :param n: int, necessary number to shift ALPHABET as cipher table
    :return: str, cipher table
    """
    a=''
    for i in range((26-n),26):
        a+=ALPHABET[i]
    for i in range(26-n):
        a+=ALPHABET[i]
    return a

def decipher(s,x):
    """
    Encrypt the string the user input
    :param s: str, string being encrypted
    :param x: str, cipher table
    """
    b=''
    for i in s:
        ch=x.find(i)
        if ch==-1:
        # When there is ' ' in the string.
            b+=i
        else:
            b+=ALPHABET[ch]
    print('The deciphered string is: '+b)

#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
