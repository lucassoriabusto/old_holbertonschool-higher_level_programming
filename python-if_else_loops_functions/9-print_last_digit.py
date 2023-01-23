#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        np = number % -10
        print(np, end="")
        return np
    else:
        print(number % 10, end="")
    return number % 10
