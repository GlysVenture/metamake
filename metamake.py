#!/bin/python3

import os
import sys

def create_make(name, make, path):
    source = open(os.path.join(os.path.dirname(__file__), make), "r")
    contents = source.read()
    source.close()
    contents = contents.replace("[name]", name)
    makefile = open(os.path.join(path, "Makefile"), "x")
    makefile.write(contents)
    makefile.close()

def main():
    directory = os.getcwd()

    create_make("bin_name", "parentmake_template", ".")

    os.mkdir(os.path.join(directory, "tests"))
    os.mkdir(os.path.join(directory, "src"))
    os.mkdir(os.path.join(directory, "bin"))
    os.mkdir(os.path.join(directory, "libs"))

    create_make("bin_name", "libmake_template", "./libs")

    if os.path.exists("./parentmake_template"):
        os.remove("parentmake_template")
    if os.path.exists("./libmake_template"):
        os.remove("libmake_template")
    if os.path.exists("./metamake.py"):
        os.remove("metamake.py")

if __name__ == "__main__":
    main()
