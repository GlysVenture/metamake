# metamake

A project setupper for C/C++ projects using make and criterion.

## Installation

Clone for first installation. You can delete the directory afterwards.

    $ git clone https://github.com/GlysVenture/metamake
    $ cd metamake
    $ bash install.sh
    [optional]
    $ rm -rf ../metamake
    
if this doesn't work it means you probably don't have a $HOME/.local/bin directory and you don't have access to /usr/bin.
Just create $HOME/.local/bin and rerun install.sh
    
To update simply do

    $ metamake --update
    
## Usage

go to or create a new directory for your project and then use metamake

    $ mkdir <my_new_dir>
    $ cd <my_new_dir>
    $ metamake <binary name>

## Project Setup Overview
    
    ProjectDirectory
    ├── Makefile
    ├── bin
    ├── libs
    │   ├── Makefile
    │   └── some_library    
    ├── src
    │   └── main.c
    └── tests
        ├── Makefile
        ├── criterion-v2.3.2
        └── tests.c


Makefile has basic **$(NAME)**, **all**, **clean**, **fclean** and **re** rules

All source files in **src** are compiled. Build files are kept in a temporary **build** directory.
Binaries are kept in **bin** directory

**release** rule recompiles all with -O3 and -march=native flags

**libs** directory is where libraries live. Each library should have its own directory with same exact name (excluding lib and .a).
Each of these directories should have a Makfile with a default rule that compiles the lib or no Makefile but an .a file.
They need also to have .h files located in ./include

**tests** dir is where tests are run and criterion lives.
If you do make tests all \*.c files in the tests directory will be compiled and ran one after the other.
An example file with Test is present, but you should check out the [criterion repo](https://github.com/Snaipe/Criterion).

## Status

/!\ first release, unstable /!\

No support for C++

Libs implementation mainly untested

Only works with static libs (.a archives)
