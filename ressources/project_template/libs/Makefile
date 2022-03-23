CFLAGS ?= -Wall -Wextra -Werror
CC = [#compiler#]
MAKEFLAGS += --no-print-directory

_COLOR := \033[1;36m
_END := \033[0m

ifeq ($(strip $(shell find ./* -maxdepth 0 -type d | wc -l)), 0)
	DIRS := 
else
	DIRS := $(shell echo */)
endif

LIBS = $(patsubst %/,lib%.a,$(DIRS))
PATHS = $(join $(DIRS),$(LIBS))
INCS = $(addsuffix include,$(DIRS))

libs:
	@for dir in $(DIRS:%/=%) ; do \
		printf "[$(_COLOR)libs$(_END)] $$dir checking...\n"; \
		if [ $$(find $$dir -maxdepth 1 -type f -name "Makefile" | wc -l) != 0 ] ; \
		then \
			$(MAKE) -e CFLAGS="$(CFLAGS)" -C $$dir > /dev/null; \
		fi \
	done

lib_names:
	@echo -n $(DIRS:%/=%)

lib_path:
	@echo -n $(PATHS)

lib_inc:
	@echo -n $(INCS)

all:	libs

clean:
	@for dir in $(DIRS:%/=%) ; do \
		if [ $$(find $$dir -maxdepth 1 -type f -name "Makefile" | wc -l) != 0 ] ; \
		then \
			printf "[$(_COLOR)libs$(_END)] cleaning $$dir\n"; \
			$(MAKE) -C $$dir clean > /dev/null; \
		fi \
	done

fclean:
	@for dir in $(DIRS:%/=%) ; do \
		if [ $$(find $$dir -maxdepth 1 -type f -name "Makefile" | wc -l) != 0 ] ; \
		then \
			printf "[$(_COLOR)libs$(_END)] full cleaning $$dir\n"; \
			$(MAKE) -C $$dir fclean > /dev/null; \
		fi \
	done

.PHONY: libs lib_names lib_inc lib_path all clean fclean
