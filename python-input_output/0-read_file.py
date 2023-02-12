#!/usr/bin/python3
"""Function that reads a text file"""


def read_file(filename=""):
    """Reads a file with open() and then prints its contents"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
