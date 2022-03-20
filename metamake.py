#!/bin/python3

import os
import shutil
import sys

def create_make(name, make, path):
    source = open(os.path.join(os.path.dirname(__file__), "templates/" + make + ".template"), "r")
    contents = source.read()
    source.close()
    contents = contents.replace("[name]", name)
    makefile = open(os.path.join(path, "Makefile"), "x")
    makefile.write(contents)
    makefile.close()

def create_file(substr, file, path):
    source = open(os.path.join(os.path.dirname(__file__), "templates/" + file + ".template"), "r")
    contents = source.read()
    source.close()
    contents = contents.replace("[substr]", substr)
    makefile = open(os.path.join(path, file), "x")
    makefile.write(contents)
    makefile.close()

def main():

    if len(sys.argv) != 2:
        print("invalid arguments, please input binary name")

    bin_name = sys.argv[1]

    directory = os.getcwd()

    create_make(bin_name, "parentmake", ".")

    os.mkdir(os.path.join(directory, "tests"))
    os.mkdir(os.path.join(directory, "src"))
    os.mkdir(os.path.join(directory, "bin"))
    os.mkdir(os.path.join(directory, "libs"))

    create_make(bin_name, "libmake", "./libs")
    create_make(bin_name, "testmake", "./tests")
    shutil.copytree(os.path.join(os.path.dirname(__file__), "criterion-v2.3.2"), "./tests/criterion-v2.3.2")
    create_file(bin_name, "main.c", "./src")
    create_file(bin_name, "tests.c", "./tests")

if __name__ == "__main__":
    main()
