#!/usr/bin/python3
"""Function that writes a string to a text file
and returns the number of characters written"""


def append_write(filename="", text=""):
    """Opens the file, if it does not exist, creates it"""
    with open(filename, "a", encoding="utf-8") as f:
        """Overwrite the content of the file if it already exists"""
        f.write(text)
        return len(text)
