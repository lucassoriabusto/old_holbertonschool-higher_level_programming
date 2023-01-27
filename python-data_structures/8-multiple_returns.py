#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        new_tupla = (len(sentence), None)
        return new_tupla
    else:
        new_tupla = (len(sentence), sentence[0])
        return new_tupla
