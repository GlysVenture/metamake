CFLAGS := -Wall -Wextra -Werror -g3
CC = [#compiler#]
MAKEFLAGS += --no-print-directory

#UNAME = $(shell uname -s)

_COLOR := \033[1;33m
_END := \033[0m

#directories
#mkdir -p is here for potentially empty directories that could be lost upon git push to remote
SRC_DIR := $(shell mkdir -p ./src && printf "./src")
TESTS_DIR := ./tests
LIBS_DIR := ./libs
BIN_DIR := $(shell mkdir -p ./bin && printf "./bin")
INC_DIR := $(shell mkdir -p ./include && printf "./include")
BUILD_DIR ?= ./build

NAME := [#name#]

SRCS = $(shell find $(SRC_DIR) -name *.[#lang#])
OBJS = $(SRCS:%=$(BUILD_DIR)/%.o)

LIBS = $(shell $(MAKE) --no-print-directory -C $(LIBS_DIR) lib_names)
LIB_FILES = $(addprefix $(LIBS_DIR)/,$(shell $(MAKE) --no-print-directory -C $(LIBS_DIR) lib_path))
LIBS_INC = $(addprefix $(LIBS_DIR)/,$(shell $(MAKE) --no-print-directory -C $(LIBS_DIR) lib_inc))

TEST_FLAGS = $(addprefix -I../,$(LIBS_INC)) -I../$(INC_DIR) $(addprefix -L../,$(LIBS)) $(addprefix -l,$(LIBS))

$(BUILD_DIR)/%.[#lang#].o : %.[#lang#]
	@printf "[$(_COLOR)make$(_END)] compiling $@...\n"
	@mkdir -p $(dir $@)
	@$(CC) -c $(CFLAGS) $(addprefix -I,$(LIBS_INC)) -I$(INC_DIR) $< -o $@

$(NAME):
	@printf "[$(_COLOR)make$(_END)] checking update status...\n"
	@if ! $(MAKE) $(BIN_DIR)/$(NAME) | grep -v "is up to date" ; then \
		printf "[$(_COLOR)make$(_END)] $@ is up to date ✅\n"; \
	fi

$(BIN_DIR)/$(NAME):	$(OBJS) $(LIB_FILES)
	@printf "[$(_COLOR)make$(_END)] linking $@\n"
	@$(CC) $(CFLAGS) $(OBJS) $(addprefix -L$(LIBS_DIR)/,$(LIBS)) $(addprefix -l,$(LIBS)) -o $(BIN_DIR)/$(NAME)

release: CFLAGS += -03 -march=native
release: fclean
release: all

tests:
	@printf "[$(_COLOR)make$(_END)] starting tests...\n"
	@$(MAKE) -e TEST_FLAGS="$(TEST_FLAGS)" -C $(TESTS_DIR)

$(LIB_FILES): library

run:
	@$(MAKE) $(BIN_DIR)/$(NAME) | grep -v "is up to date" || true
	@printf "[$(_COLOR)make$(_END)] running $(NAME)\n"
	@$(BIN_DIR)/$(NAME)


library:
	@$(MAKE) -e CFLAGS="$(CFLAGS)" -C $(LIBS_DIR)

all:	
	@$(MAKE) $(NAME) && $(MAKE) tests

clean:
	@rm -rf $(BUILD_DIR)
	@$(MAKE) -C $(LIBS_DIR) fclean
	@printf "[$(_COLOR)make$(_END)] clean done\n"

fclean:
	@rm -rf $(BUILD_DIR)
	@rm -rf $(BIN_DIR)/$(NAME)
	@$(MAKE) -C $(LIBS_DIR) fclean
	@printf "[$(_COLOR)make$(_END)] fclean done\n"

re: fclean
re:	all

.PHONY: all fclean clean library re release tests run
