# -*- coding: utf-8 -*-

import string
from optparse import OptionParser
import sys

def setup_dict(size, length, tmp):
    tmp2 = list(tmp)
    length = int(length)
    for i in range(length):
        tmp1 = list(tmp2)
        tmp2 = []
        for x in tmp:
            for y in tmp:
                tmp2.append(x+y)
                if size == "full":
                    yield x+y
                elif size == "length":
                    if i == length-1:
                        yield x+y
                    else:
                        yield ""


def create_write_dict_to_file(size, length, dict):
    file = open("dict.txt", "w+")
    for x in setup_dict(size, length, list(dict)):
        if x != "":
            file.write(x+"\n")
            print x+"\n"



def dict_choice(size, length, type):
    alph = "abcdefghijklmnopqrstuvwxyz"
    alph += string.upper(alph)
    num  = "0123456789"
    spec_chars = " &é\"'(§è!çà)-_^¨$*ù%`£+=/:.;?,|#@\\€"
    if type == "alph_num":
        create_write_dict_to_file(size, length, alph+num)
    elif type == "alph_num_spe-chars":
        create_write_dict_to_file(size, length, alph+num+spec_chars)
    elif type == "alph":
        create_write_dict_to_file(size, length, alph)

def main(size, length, type):
    dict_choice(size, length, type)

if __name__ == '__main__':
    option_parser = OptionParser()
    option_parser.add_option("-s", "--size", dest="size",
                      help="The size of the values of the dictionary.\n Either full dictionary it means the size is from 2 to length or just the length size. \n values: full | length")

    option_parser.add_option("-l", "--length", dest="length",
                      help="The length of the largest value.\n")

    option_parser.add_option("-t", "--type", dest="type",
                      help="The type of the dictionary.\n Values: alph | alph_num | alph_num_spe-chars\n")

    (options, args) = option_parser.parse_args()
    if options.size is None or options.length is None or options.type is None:
        print("Missing argument.")
        print("Please use -h for more information.")
        print("\t"+sys.argv[0]+ " -h")
        exit("\n")

    main(options.size, options.length, options.type)
