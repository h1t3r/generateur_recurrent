# -*- coding: utf-8 -*-

import string


def setup_dict(length, tmp, tmp1, dict):
    print length
    length = length-1
    if length == 1:
        for x in tmp:
            yield x
    t = [x+y for x in tmp for y in tmp1]
    for x in setup_dict(length, list(tmp), list(t), dict):
        yield x

def create_write_dict_to_file(length, dict_a, dict_n, dict_s):
    if dict_a and dict_n and dict_s:
        tmp = [ x for x in dict_a + dict_n + dict_s ]
    elif dict_a and dict_n:
        tmp = [ x for x in dict_a + dict_n ]
    elif dict_a:
        tmp = [ x for x in dict_a]

    file = open("dict.txt", "w+")
    for x in setup_dict(length, list(tmp), list(tmp), list(tmp)):
        print x+"\n"
        file.write(x+"\n")
"""
    tmp = setup_dict(length, list(tmp), list(tmp), list(tmp))
    for x in tmp:
        print x+"\n"
        file.write(x+"\n")
"""
def dict_choice(choice):
    alph = "abcdefghijklmnopqrstuvwxyz"
    alph += string.upper(alph)
    num  = "0123456789"
    spec_chars = " &é\"'(§è!çà)-_^¨$*ù%`£+=/:.;?,"
    if choice == "alph_num":
        create_write_dict_to_file(8, alph, num, "")
    elif choice == "alph_num_spe-chars":
        create_write_dict_to_file(8, alph, num, spec_chars)
    elif choice == "alph":
        create_write_dict_to_file(14, alph, "", "")

def main():
    dict_choice("alph_num")

if __name__ == '__main__':
    main()
