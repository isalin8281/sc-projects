"""
File: boggle.py
Name: Isabelle
----------------------------------------
The program recursively finds all vocabularies which
exist in boggle that program asks user inputs.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
# Contains the chars we would like to ignore while processing the words
PUNCTUATION = '.,;!?#&-\'_+=/\\"@$^%()[]{}~'

# Global variable
Dictionary_lst = []        # List, which program will put words got from FILE into
Row = []                   # A dict, which program will put letters that user input into
found_lst = []             # Record all vocabularies the programs found in boggle


def main():
    """
    Ask user inputs four rows and four letters in each row to make boggle,
    and find all vocabularies which exists in boggle
    """
    # User has to input four rows and four letter in each row
    read_dictionary()
    for i in range(4):
        row = str(input(str(i + 1) + ' row of letters: ')).lower()
        # Check if row which user inputs is illegal input
        ans = illegal_input_test(row)
        if ans is False:
            print('Illegal input')
            break
        # Add row into a list
        boggle(row)
    # Find all vocabularies which exists in boggle
    search_word()
    print("There are " + str(len(found_lst)) + " words in total.")


def illegal_input_test(row):
    """
    Check if the format user inputs is illegal format
    :param row: str, the user inputs
    :return: bool
    """
    if 7 <= len(row) < 9:
        for i in range(len(row)):
            # Check if any punctuation is in row
            if row[i] in PUNCTUATION:
                return False
            # Check if a space exists between each letter
            elif i % 2 == 1:
                if row[i] != ' ':
                    return False
        return True
    else:
        return False


def boggle(row):
    """
    Add each row to list
    :param row: string, user input
    :return: a string, clean space inside row
    """
    global Row
    word = ''
    # Eliminate space between letters in row
    for ch in row:
        if ch.islower():
            word += ch
    # Add to list
    Row.append(word)


def search_word():
    """
    Find vocabulary which exists in boggle
    """
    word = ''
    # list, record letters which already exists in word
    exist_lst = []
    # Run each letter in (list)Row
    for i in range(len(Row)):
        for j in range(len(Row[i])):
            search_word_helper(i, j, word, exist_lst)


def search_word_helper(i, j, word, lst):
    """
    Find vocabulary and add to found_lst
    :param i: int, order of rows
    :param j: int, order of letters in row
    :param word: empty str
    :param lst: list, record letters which already exists in word
    """
    global found_lst
    # The vocabulary nus have more than four letters
    # Check if the vocabulary already exists in (list)found_lst
    if len(word) >= 4 and word in Dictionary_lst and word not in found_lst:
        # add vocabulary to (list)found_lst
        found_lst.append(word)
        print('Found ' + '"' + word + '"')
    else:
        # Check if sub-string could become a vocabulary
        ans = has_prefix(word)
        if ans is True:
            # Start to make vocabulary
            for x in range(-1, 3, 1):
                for y in range(-1, 3, 1):
                    # i_x stands for order of rows
                    i_x = i + x
                    # y stands for order of letters in rows
                    j_y = j + y
                    # Check if i_x is out of index
                    if 0 <= i_x < (i+2) and i_x < len(Row) and (i_x, j_y) not in lst:
                        # Check if j_y is out of index
                        if 0 <= j_y < (j+2) and j_y < len(Row[i_x]):
                            lst.append((i_x, j_y))
                            # Choose
                            word += Row[i_x][j_y]
                            # Explore
                            search_word_helper(i_x, j_y, word, lst)
                            # Un-choose
                            word = word[:len(word)-1]
                            lst.pop()
        else:
            return


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    global Dictionary_lst
    # Open file
    with open(FILE, 'r') as f:
        # Run each line in FILE
        for line in f:
            word = get_word(line)
            # add word into lst
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


def has_prefix(sub_s):
    """
    Check if sub-string could become a vocabulary
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
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
