#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
else
	python3 "$HOME/.metamake/metamake.py" $1
fi
