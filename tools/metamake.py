#!/bin/python3

#todo cpp
import os
import shutil
import sys

#metamake default context
class Options():
    bin_name = "a.out"
    lang = "c"
    compiler = "gcc"
    directory = None

#prints --help message
def help():
    print("usages:")
    print("metamake [options] <empty_target_dir>")
    print(" options:")
    print("  -n --name <executable_name>")
    print("  -c --compiler <compiler>")
    print("  -cpp")
    print("metamake [options]")
    print(" options:")
    print("  --help")
    print("  --update")

#parses input arguments into options
def parse_args():
    options = Options()

    it = iter(sys.argv)
    next(it)
    for word in it:
        if word == "--help":
            help()
            sys.exit()
        elif word == "-n" or word == "--name":
            temp = next(it, None)
            if temp == None:
                print("error: name arg missing, metamake --help")
                sys.exit()
            options.bin_name = temp
        elif word == "-c" or word == "--compiler":
            temp = next(it, None)
            if temp == None:
                print("error: compiler arg missing, metamake --help")
                sys.exit()
            options.compiler = temp
        elif word == "-cpp":
            options.lang = "cpp"
            options.compiler = "g++"
        else:
            if options.directory == None:
                options.directory = word
            else:
                print("error: too many arguments, metamake --help")
                sys.exit()

    if options.directory == None:
        print("error: directory arg missing, metamake --help")
        sys.exit()
    return options

#replaces [#<something>#] symbols in file by corresponding options fields
def parse_file(filepath, options):
    source = open(filepath, "r")
    contents = source.read()
    source.close()

    contents = contents.replace("[#name#]", options.bin_name)
    contents = contents.replace("[#compiler#]", options.compiler)
    contents = contents.replace("[#lang#]", options.lang)
    if options.lang == "cpp":
        contents = contents.replace("[#std_cpp#]", "-std=c++11")
    else:
        contents = contents.replace("[#std_cpp#]", "")

    not_source = open(filepath, "w")
    not_source.write(contents)
    not_source.close()

#creates directory copying the template and parsing files using the options provided
def dir_from_options(options):
    shutil.copytree(os.path.join(os.path.dirname(__file__), "../ressources/project_template"), options.directory)

    os.mkdir(options.directory + "/src")
    os.mkdir(options.directory + "/bin")
    os.mkdir(options.directory + "/include")

    if options.lang == "c":
        shutil.copy(os.path.join(os.path.dirname(__file__), "../ressources/templates/main.c.template"), options.directory + "/src/main.c")
        shutil.copy(os.path.join(os.path.dirname(__file__), "../ressources/templates/tests.c.template"), options.directory + "/tests/test.c")
    elif options.lang == "cpp":
        shutil.copy(os.path.join(os.path.dirname(__file__), "../ressources/templates/main.cpp.template"), options.directory + "/src/main.cpp")
        shutil.copy(os.path.join(os.path.dirname(__file__), "../ressources/templates/tests.cpp.template"), options.directory + "/tests/test.cpp")

    for path, subdirs, files in os.walk(options.directory):
        if not ("criterion" in path) :
            for name in files:
                parse_file(os.path.join(path, name), options)

def main():

    options = parse_args()

    print("creating project in: " + options.directory)
    print("named: " + options.bin_name)
    print("language: " + options.lang)
    print("using compiler: " + options.compiler)

    dir_from_options(options)

    print("Creation sucessfull!")

if __name__ == "__main__":
    main()
