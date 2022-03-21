# metamake

A project setup tool for C/C++ projects using make and criterion.

![](https://img.shields.io/badge/platform-linux%20%7C%20macOs-lightgrey) ![](https://img.shields.io/badge/python-v3.8-blue)
## Installation

Clone for first installation. You can delete the directory afterwards.

    $ git clone https://github.com/GlysVenture/metamake
    $ cd metamake
    $ make install
    [optional]
    $ rm -rf ../metamake
    
if this doesn't work it means you probably don't have a $HOME/.local/bin directory and you don't have access to /usr/bin.
Just create $HOME/.local/bin and rerun make install
    
To update simply do

    $ metamake --update
    
## Usage

```
usages:
metamake [options] <empty_target_dir>
 options:
  -n --name <executable_name>
  -c --compiler <compiler>
  -cpp
metamake [options]
 options:
  --help
  --update
```

## Project Setup Overview
    
    ProjectDirectory
    ├── Makefile
    ├── bin
    ├── include
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
They need also to have .h/.hpp files located in ./include

**tests** dir is where tests are run and criterion lives.
If you do make tests all \*.c/.cpp files in the tests directory will be compiled and ran one after the other.
An example file with Test is present, but you should check out the [criterion repo](https://github.com/Snaipe/Criterion).

**run** rule runs the binary. **all** compiles, tests and then runs.

## Philosophy

This is a one and done kind of utility. It is not a build tool. It just sets up Makefiles and directories, maintenance and changes are up to you.

## Status

Libs implementation might be untested

Only works with static libs (.a archives)

## Ressources

[GNU Make manual](https://www.gnu.org/software/make/manual/make.html)

[Criterion Youtube Tutorial](https://youtu.be/JarMkGWTF8Y)

[Criterion documentation](https://criterion.readthedocs.io/en/master/)

## Credits

[Criterion](https://github.com/Snaipe/Criterion)
