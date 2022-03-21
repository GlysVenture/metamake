CFLAGS ?= -Wall -Wextra -Werror
CC = [#compiler#]
MAKEFLAGS += --no-print-directory

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
		printf "[`tput setaf 6`libs`tput sgr0`] $$dir checking...\n"; \
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
			printf "[`tput setaf 6`libs`tput sgr0`] cleaning $$dir\n"; \
			$(MAKE) -C $$dir clean > /dev/null; \
		fi \
	done

fclean:
	@for dir in $(DIRS:%/=%) ; do \
		if [ $$(find $$dir -maxdepth 1 -type f -name "Makefile" | wc -l) != 0 ] ; \
		then \
			printf "[`tput setaf 6`libs`tput sgr0`] full cleaning $$dir\n"; \
			$(MAKE) -C $$dir fclean > /dev/null; \
		fi \
	done

.PHONY: libs lib_names lib_inc lib_path all clean fclean
