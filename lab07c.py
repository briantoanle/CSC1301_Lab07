"""
Program: CS 1301 Lab 06
Author: Toan Le
Description: This program will read a positive integer and
    express it as the sum of powers of 2.
"""


def main():
    # Read user's input and store it as an integer in a variable called i_num.
    i_num = int(input("Please enter a positive integer "))
    # Outer loop:
    # while i_num is larger than zero:
    while i_num > 0:
        # Initialize n and two_to_n.
        n = 2
        two_to_n = 2**n
        # Do all the stuff you were doing before to find n and two_to_n.
        # Remember that two_to_n is the largest power of 2 less than i_num.
        while two_to_n < i_num:
            n +=1
            two_to_n *= 2
        if two_to_n > i_num:
            n -= 1
            two_to_n /= 2
        i_num = i_num - two_to_n

        if i_num == 0:
            print('2**'+ str(n))
        else:
            print(f'2**{n}', "+ ", end="")


main()
