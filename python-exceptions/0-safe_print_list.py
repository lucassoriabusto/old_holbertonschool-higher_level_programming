#!/usr/bin/python3i
def safe_print_list(my_list=[], x=0):
    contador = 0
    for n in range(x):
        try:
            print(my_list[n], end="")
            contador += 1
        except IndexError:
            break
    print("")
    return contador
