"""
File: anagram.py
Name: Isabelle
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variable
Dictionary_lst = []           # List, which program will put words from FILE into
anagrams_lst = []             # List, which program will put results of into
s_dict = {}                   # Dict, record occurrence of each letter in s which user inputs


def main():
    global anagrams_lst, s_dict
    # get words from FILE and put into Dictionary_lst
    read_dictionary()
    print('Welcome to stanCode \"Anagram Generator\" (or ' + EXIT + ' to quit)')
    while True:
        # Clean anagrams_lst and s_dict each loop
        anagrams_lst = []
        s_dict = {}
        s = input('Find anagrams for: ')
        # Count occurrence of each letter in s
        for ch in s:
            if ch in s_dict:
                s_dict[ch] += 1
            else:
                s_dict[ch] = int(1)
        # User ends the program
        if s == EXIT:
            break
        else:
            # Find anagrams in s
            find_anagrams(s)


def read_dictionary():
    """
    Add words from FILE to (lst)Dictionary_lst
    """
    global Dictionary_lst
    # Open file
    with open(FILE, 'r') as f:
        # Run each line in file
        for line in f:
            word = get_word(line)
            # Add word into lst
            Dictionary_lst.append(word)


def get_word(line):
    """
    Get word from each line
    :param line: line from FILE
    :return: str, word got from line
    """
    word = ''
    # Run each letter in line
    for ch in line:
        if ch.islower():
            word += ch
    return word


def find_anagrams(s):
    """
    Look up each anagram in Dictionary_lst, and print result
    :param s: str, a word the user inputs
    """
    # empty string which program will put anagram into
    word = ''
    find_anagrams_helper(s, word)
    print(str(len(anagrams_lst)) + ' anagrams: ', end='')
    print(anagrams_lst)


def find_anagrams_helper(s, word):
    """
    Make anagrams and look up each anagrams in Dictionary_lst
    :param s: str, a word the user inputs
    :param word: empty string
    """
    global anagrams_lst
    # Base case
    if len(word) == len(s):
        # Check if word exists in Dictionary_lst and if word already exists in anagrams_lst
        if word in Dictionary_lst and word not in anagrams_lst:
            print('Searching...')
            print('found: ' + word)
            # Add each word into lst
            anagrams_lst.append(word)
    else:
        # Check if substring exists in Dictionary_lst
        ans = has_prefix(word)
        if ans is True:
            # Run each letter in s
            for ch in s:
                if s_dict[ch] != 0:
                    # Choose
                    word += ch
                    s_dict[ch] -= 1
                    # Explore
                    find_anagrams_helper(s, word)
                    # Un-choose
                    word = word[0:len(word) - 1]
                    s_dict[ch] += 1
        else:
            return
  

def has_prefix(sub_s):
    """
    Check if sub_s exists in vocabularies
    :param sub_s: str
    :return: bool
    """
    # Word is empty string
    if len(sub_s) == 0:
        return True
    else:
        # Run each word in Dictionary_lst
        for word in Dictionary_lst:
            if sub_s in word[:len(sub_s)]:
                return True
        return False
    

if __name__ == '__main__':
    main()
