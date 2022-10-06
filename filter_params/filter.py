#!/bin/python3

'''
    This script take a file containing urls as an argument and find and filter
    query params.
'''

from urllib.parse import urlparse, unquote
import sys

fetched_paths = []
fetched_queries = []
params = []
file = sys.argv[1]

valid_symbols = ["!","@","#","%","^","&","*","(",")","-","+","=","{","}","[","]","/",":",";","."]


def file_input(file):
    with open(file) as f:
        for line in f:
            link = urlparse(line)
            url_path = link.path
            queries = unquote(link.query)
            if (url_path != "/") and (url_path != ""):
                fetched_paths.append(url_path)
            if (queries != "/") and (queries != ""):
                fetched_queries.append(queries)


def grab_params(x):
    for i in x:
        v = i.partition("=")
        params.append(v[0])


def uniq_param(data):
    list_set = set(data)
    uniq_value = (list(filter(None, list_set)))
    for value in uniq_value:
        if len(value) < 15:
            if not value.isnumeric() and value.isalpha():
                if (value != "") and (value != urlparse(value)):
                    if not value.startswith(tuple(valid_symbols)):
                        x = value.strip("\n")
                        x.strip()
                        print(x)


if __name__ == "__main__":
    if sys.argv[1]:
        file_input(sys.argv[1])
        grab_params(fetched_queries)
        uniq_param(params)
