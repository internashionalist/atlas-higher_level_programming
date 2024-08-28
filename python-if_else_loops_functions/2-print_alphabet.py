#!/usr/bin/python3
ascii_value = 97
while ascii_value < 123:
    form_out = "{0}" .format(chr(ascii_value))
    print(form_out, end="")
    ascii_value += 1
