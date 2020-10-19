"""
File: babynames.py
Name: Isabelle
----------------------------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This file reads information from files, and adds data into dict
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    # see if name exists in dict
    if name in name_data:
        # see if year exists in dict
        if year in name_data[name]:
            # get rank in dict
            value = name_data[name][year]
            # compare ranks
            if int(rank) < int(value):
                # replace lower with higher rank
                name_data[name][year] = rank
        else:
            name_data[name][year] = rank
    else:
        name_data[name] = {}
        name_data[name][year] = rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    # open file
    with open(filename, 'r') as f:
        # When x is True, function runs the first line to get data-year in file.
        # When x is False, function runs the rest of lines to get data (year, rank, and names).
        x = True
        # run lines to get data from file
        for line in f:
            if not x:
                # rank
                rank = get_digit(line)
                # first name in line
                name1 = get_name1(line).strip()
                # second name in line
                name2 = get_name2(line).strip()
                # add data into name_data dict
                add_data_for_name(name_data, year, rank, name1)
                add_data_for_name(name_data, year, rank, name2)
            # run first line in file
            else:
                # year
                year = get_digit(line)
                x = False


def get_digit(word):
    """
    : param word: line

    This method gets digit in line

    : return: string
    """
    # empty string
    string = ''
    for ch in word:
        if ch.isdigit():
            string += ch
    return string


def get_name1(word):
    """
    : param word: line

    This method splits line and gets first name in line

    : return : string, name
    """
    # empty string
    name_1 = ''
    for i in range(len(word)):
        if word[i] == ',':
            for j in range((i+1), len(word)):
                if word[j] == ',':
                    name_1 = word[(i+1):j]
    return name_1


def get_name2(word):
    """
    : param word: line

    This method splits line and gets second name in line

    : return : string, name
    """
    # empty string
    name_2 = ''
    for i in range(len(word)):
        if word[i] == ',':
            for j in range((i+1),len(word)):
                if word[j] == ',':
                    name_2 = word[(j+1):]
    return name_2


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    # empty dict
    name_data = {}
    #
    for file in filenames:
        # Read data from all files and put inf into name_data(dict)
        add_file(name_data, file)
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    # turn each word into lowercase
    target = target.lower()
    # empty list
    names = []
    # run each name in name_data dict
    for name in name_data:
        # turn each word into lowercase
        name_lower = name.lower()
        # search name
        if target in name_lower:
            # list of all names which contain target
            names += [name]
    return names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
