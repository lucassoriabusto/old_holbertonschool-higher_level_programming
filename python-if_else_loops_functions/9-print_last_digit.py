#!/usr/bin/python3
def print_last_digit(number):
    #number = -1024
    if number < 0:
        np = number % -10
        print(np, end="")
        return np
    elif: number >= 0:
        print(number % 10, end="")
        return number % 10
