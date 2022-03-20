#!/bin/bash

if [ $1 = --update ]; then
	git -C $HOME/.metamake pull
	echo "metamake successfully updated"
	exit
fi

if [ "$#" -ne 1 ]; then
    echo "error: illegal number of parameters"
else
	python3 "$HOME/.metamake/metamake.py" $1
fi
