# -*- coding: utf-8 -*-

import string
from optparse import OptionParser
import sys

def setup_dict(size, startlength, length, tmp):
    tmp2 = list(tmp)
    length = int(length)
    startlength = int(startlength)
    for i in range(1, length+1):
        tmp1 = list(tmp2)
        tmp2 = []
        for x in tmp1:
            for y in tmp:
                tmp2.append(x+y)
                if size == "full":
                    yield x+y
                elif size == "length":
                    if i == length:
                        yield x+y
                elif size == "section":
                    if i >= startlength-1:
                        yield x+y



def create_write_dict_to_file(size, startlength, length, dict):
    print("ok")
    file = open("dict.txt", "w+")
    for x in setup_dict(size, startlength, length, list(dict)):
        file.write(x+"\n")
        print(x+"\n")



def dict_choice(size, startlength, length, dtype):
    alph = "abcdefghijklmnopqrstuvwxyz"
    alph += alph.upper()
    num  = "0123456789"
    spec_chars = " &é\"'(§è!çà)-_^¨$*ù%`£+=/:.;?,|#@\\€"
    print(dtype)
    if dtype == "alph_num":
        print("in")
        create_write_dict_to_file(size, startlength, length, alph+num)
    elif dtype == "alph_num_spe-chars":
        create_write_dict_to_file(size, startlength, length, alph+num+spec_chars)
    elif dtype == "alph":
        create_write_dict_to_file(size, startlength, length, alph)

def main(size, length, dtype, startlength):
    print("ok")
    dict_choice(size, startlength, length, dtype)

if __name__ == '__main__':
    option_parser = OptionParser()
    option_parser.add_option("-s", "--size", dest="size",
                      help="The size of the values of the dictionary.\n Full \
                      dictionary it means the size is from 2 to length or just \
                      the \"length\" size or a section from x to x+length. \n \
                      values: full | section | length")

    option_parser.add_option("-a", "--startlength", dest="startlength",
                      help="From wich start the length of the dictionary.\n")

    option_parser.add_option("-l", "--length", dest="length",
                  help="The length of the largest value.\n")

    option_parser.add_option("-t", "--type", dest="dtype",
                      help="The type of the dictionary.\n Values: alph | alph_num | alph_num_spe-chars\n")

    (options, args) = option_parser.parse_args()
    if options.size is None or options.length is None or options.dtype is None:
        print("Missing argument.")
        print("Please use -h for more information.")
        print("\t"+sys.argv[0]+ " -h")
        exit("\n")


    main(options.size, options.length, options.dtype, options.startlength)
