"""
File: complement.py
Name: Isabelle
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    The program will find the complement of DNA strand the user input.
    """
    dna=input("Please gibe me a DNA strand and I'll find the complement: ").upper()
    new_dna=build_complement(dna)

def build_complement(dna):
    ans=''
    for i in dna:
        if i=='A':
            ans+='T'
        elif i=='T':
            ans+='A'
        elif i=='C':
            ans+='G'
        elif i=='G':
            ans+='C'
    print('The complement of '+ dna+' is '+ ans)



###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
