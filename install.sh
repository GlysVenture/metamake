#!/bin/bash

if [ -d $HOME/.metamake ]; then
	cp -r . $HOME/.metamake
else
	echo "error: $$HOME/.metamake already exists. update metamake with --update"
	exit
fi

if [ -d $HOME/.local/bin ]; then
	ln -s $HOME/.metamake/metamake.sh $HOME/.local/bin/metamake
	echo 'metamake installed in $HOME/.local/bin/metamake -> $HOME/.metamake/metamake.sh'
elif mkdir /usr/bin/metamake; then
    rmdir /usr/bin/metamake
    ln -s $HOME/.metamake/metamake.sh usr/bin/metamake
    echo 'metamake installed in usr/bin/metamake -> $HOME/.metamake/metamake.sh'
else
	echo "error: couldn't create symlink. installation cancelled"
	rm -r $HOME/.metamake
fi
