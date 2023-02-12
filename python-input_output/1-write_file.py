#!/usr/bin/python3
"""Function that writes a string to a text file
and returns the number of characters written"""


def write_file(filename="", text=""):
    """Opens the file, if it does not exist, creates it"""
    with open(filename, "w", encoding="utf-8") as f:
        """Overwrite the content of the file if it already exists"""
        f.write(text)
        return len(text)
