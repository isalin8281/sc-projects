"""
File: hailstone.py
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, as defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Calculate the number of steps to make n reach 1 and show a process of calculation.
    """
    print('This program computes Hailstone sequences.')
    print(' ')
    n=int(input('Enter a number: '))
    x=0
    #x stands for the number of steps to make n reach 1.
    if n==1:
        print('It took 0 step to reach 1.')
    else:
        while True:
            if n==1:
                break
            elif n%2==1:
            #n is odd.
                x+=1
                n=int(3*n+1)
                a=int((n-1)/3)
                print(str(a) + ' is odd, so I make 3n+1: ' + str(n))
            else:
            #n is even.
                x+=1
                n=int(n/2)
                b=2*n
                print(str(b) + ' is even, so I take half: ' + str(n))
        print('It took '+str(x)+' steps to reach 1.')






###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
