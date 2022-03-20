CFLAGS = -Wall -Wextra -Werror
CC = gcc

SRC_DIR ?= ../src
OBJ_DIR ?= ../build

UNAME = $(shell uname -s)

TEST_FLAGS ?=

SRCS = $(shell find $(SRC_DIR) -name *.c)
OBJS = $(SRCS:%=$(OBJ_DIR)/%.o)

TESTS = $(shell find . -name *.c)
BIN_DIR = ./bin
TEST_BINS = $(patsubst ./%.c, $(BIN_DIR)/%, $(TESTS))
ifeq ($(UNAME), Linux)
	CRITERION_DIR = $(dir $(shell find criterion* -type f -name "libcriterion.so"))
else
	CRITERION_DIR = $(dir $(shell find criterion* -type f -name "libcriterion.dylib"))
endif
CRITERION_INC = $(shell find $(CRITERION_DIR:%/lib/=%) -type d -name include)

all:	$(TEST_BINS)
	@for test in $(TEST_BINS); do \
		export "DYLD_LIBRARY_PATH=$(shell pwd)/$(CRITERION_DIR)" ; \
		export "LD_LIBRARY_PATH=$(shell pwd)/$(CRITERION_DIR)" ; \
		printf "[`tput setaf 1`test`tput sgr0`] running $$test\n" ; \
		./$$test || true; \
	done
	@$(MAKE) clean

$(BIN_DIR)/%: ./%.c
	@mkdir -p $(dir $@)
	@$(CC) $(CFLAGS) $< $(OBJS) -L$(CRITERION_DIR) -lcriterion -o $@ -I$(CRITERION_INC) $(TEST_FLAGS)

clean:
	@rm -rf $(BIN_DIR)
	@printf "[`tput setaf 1`test`tput sgr0`] clean done\n"

.PHONY: all clean
