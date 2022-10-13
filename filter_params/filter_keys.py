#! /usr/bin/python3

'''
 Pass file containing key params fetched using unfurl or something like that to filter the useful keys only.
'''

import sys
from urllib.parse import urlparse

valid_symbols = ["!", "@", "#", "%", "^", "&", "*", "(", ")", "-", "+", "=", "{", "}", "[", "]", "/", ":", ";", "."]

file_data = []

with open(sys.argv[1], "r") as file:
    for line in file:
        value = line.strip()
        file_data.append(value)


def main():
    keys = (list(set(file_data)))
    for key in keys:
        if len(key) < 15 and (key != ""):
            if not key.isnumeric() and key.isalpha():
                if not key.startswith(tuple(valid_symbols)):
                    if urlparse(key):
                        print(key)


if __name__ == "__main__":
    main()

