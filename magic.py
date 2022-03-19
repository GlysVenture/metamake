#!/bin/python3

import os
import sys

def create_make(name):
    contents = "CFLAGS := -Wall -Wextra -Werror\n\
CC ?= gcc\n\
MAKEFLAGS += --no-print-directory\n\
\n\
NAME = [name]\n\
\n\
UNAME = $(uname -s)\n\
\n\
#directories\n\
SRC_DIR ?= ./src\n\
TESTS_DIR ?= ./tests\n\
LIBS_DIR ?= ./libs\n\
BIN_DIR ?= ./bin\n\
INC_DIR := ./includes\n\
BUILD_DIR ?= ./build\n\
\n\
SRCS = $(find $(SRC_DIR) -name *.c)\n\
OBJS = $(SRCS:%=$(BUILD_DIR)/%.o)\n\
\n\
$(BUILD_DIR)/%.c.o $: %.c\n\
    @echo Compiling $@\n\
    @mkdir -p $(dir $@)\n\
    @$(CC) -c $(CFLAGS) $< -o $@\n\
\n\
\n"
    contents = contents.replace("[name]", name)
    print(contents)
    sys.exit()
    makefile = open("Makefile", "x")
    makefile.write(contents)
    makefile.close()


directory = os.getcwd()

create_make("bin_name")

#temporary
sys.exit()

os.mkdir(os.path.join(directory, "tests"))
os.mkdir(os.path.join(directory, "src"))
os.mkdir(os.path.join(directory, "bin"))
os.mkdir(os.path.join(directory, "libs"))


