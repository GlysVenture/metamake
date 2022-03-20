#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "error: illegal number of parameters"
    exit
fi

if [ $1 = --update ] ; then
	git -C $HOME/.metamake restore $HOME/.metamake > /dev/null
	if git -C $HOME/.metamake pull > /dev/null ; then
		echo "error: failed to update metamake"
	else
		echo "metamake successfully updated"
	fi
	exit
fi

python3 "$HOME/.metamake/metamake.py" $1
