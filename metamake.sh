#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "error: illegal number of parameters"
    exit
fi

if [ $1 = --update ] ; then
	git -C $HOME/.metamake restore $HOME/.metamake > /dev/null
	if git -C $HOME/.metamake pull > /dev/null ; then
		echo "metamake is up to date"
	else
		echo "sucessfully updated metamake"
	fi
	exit
fi

python3 "$HOME/.metamake/metamake.py" $1
