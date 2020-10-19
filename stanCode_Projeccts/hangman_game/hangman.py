"""
File: hangman.py
Name: Isabelle
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    The user plays game to guess the word.
    One character each round.
    Only 7 guesses.
    """
    a=random_word()
    b=dashed(a)
    input_ch(a,b)

def dashed(a):
    """
    Show user the number of word.
    :param a: str, random word
    :return: str, the number of random word
    """
    x=''
    for i in range(len(a)):
        x+='_'
    print('The word looks like: '+x)
    return x

def input_ch(a,b):
    """
    User starts to guess word.
    If input is correct, show the updated word.
    :param a: str, random word
    :param b: str, the number of random word
    """
    x=7
    y=0
    ans=b
    c=''
    while True:
        print('You have '+str(x)+' guesses left.')
        ch=input('Your guess: ').upper()
        c=ans
        if len(ch)==0:
        # Illegal format
            print('Illegal format.')
        if len(ch)>1:
        # Illegal format
            print('Illegal format.')
        elif ch.isdigit():
        # Illegal format
            print('Illegal format')
        elif ch in a:
        # The character user guessed is right
            x-=1
            y+=1
            for j in range(len(a)):
                if ch==a[j]:
                # ans shows the correct character the user guesses
                    ans=ans[0:j]
                    ans+=a[j]
                    if y==1:
                        ans+=b[j+1:]
                    else:
                        ans+=c[j+1:]
            print('You are correct!')
            if ans==a:
            # asn==a means the user win the game, skip to line 88
                pass
            else:
                print('The word looks like: ' + ans)
        else:
        # The character user guessed is wrong
            x-=1
            y+=1
            print('There is no ' + ch + "'s in the word.")
            print('The word looks like: ' + ans)
        if ans == a:
            print('You win!!')
            print('The word was: ' + a)
            break
        elif y==7:
        # User loses the game.
                print('You are completely hung:(')
                print('The word was: ' + a)
                break

def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
