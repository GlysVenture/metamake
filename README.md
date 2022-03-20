# metamake

A project setupper for C/C++ projects using make and criterion.

## Installation

    ```bash
    $ git clone https://github.com/GlysVenture/metamake
    $ cd metamake
    $ bash install.sh
    ```
## Usage

go to or create a new directory for your project and then use metamake

    ```bash
    $ mkdir <my_new_dir>
    $ cd <my_new_dir>
    $ metamake <binary name>
    ```

## Project Setup Overview

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

Doesn't check if target dir is empty

Only works with static libs (.a archives)
