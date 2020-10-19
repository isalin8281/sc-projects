"""
File: similarity.py
Name: Isabelle
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    The program compares short dna sequence (s2) with long dna sequence (s1)
    ,and find the best match in s1.
    """
    s1 = input('Please give me a DNA sequence to search: ').upper()
    s2 = input('What DNA sequence would you like to match? ').upper()
    search(s1, s2)

def search(s1, s2):
    x=s1.find(s2)
    z=0
    a=''
    b=''
    ans=''
    if x==-1:
    # Look for the most similar dna strand in s1
        for i in range(len(s1)-len(s2)+1):
            y=0
            for j in range(len(s2)):
                a=s1[i+j]
                # a stands for each dna in long dna sequence
                b=s2[j]
                # b stands for each dna in short dna sequence
                if a==b:
                    y+=1
                    # y stands for the number of same dna in s1
            if z>y:
                pass
            else:
                z=y
                ans=s1[i:i+len(s2)]
                # ans is most similar dna strand in s1
        print('The best match is '+ ans)
    else:
    #The program find exactly same dna strand in s1
        print('The best match is '+ s2)



###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
