#!/usr/bin/python3
def max_integer(my_list=[]):
    largest_number = my_list[0]
    for n in my_list:
        if n > largest_number:
            largest_number = n
    return largest_number
