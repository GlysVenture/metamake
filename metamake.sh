#!/bin/bash

if [ $1 = --update ]; then
	if [ git -C $HOME/.metamake pull > /dev/null ] ; then
		echo "error: failed to update metamake"
	else
		echo "metamake successfully updated"
	fi
	exit
fi

if [ "$#" -ne 1 ]; then
    echo "error: illegal number of parameters"
else
	python3 "$HOME/.metamake/metamake.py" $1
fi
