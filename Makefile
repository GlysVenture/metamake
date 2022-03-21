
install:
	@bash tools/install.sh

uninstall:
	@bash tools/uninstall.sh

update:
	@git pull

#this is for github actions, not for use
setup:
	mkdir -p $$HOME/.local/bin
	export PATH="$$PATH:$$HOME/.local/bin"
	metamake dir

tests:
	$(MAKE) -C dir
	$(MAKE) -C dir
	$(MAKE) -C dir clean
	$(MAKE) -C dir tests
	$(MAKE) -C dir fclean
	$(MAKE) -C dir run
	$(MAKE) -C dir all
	$(MAKE) -C dir re
	$(MAKE) -C dir release
