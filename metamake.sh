#!/bin/bash

if [ $1 = --update ] ; then
	git -C $HOME/.metamake restore $HOME/.metamake > /dev/null
	if git -C $HOME/.metamake pull > /dev/null ; then
		echo "[`tput setaf 6 && tput bold`metamake`tput sgr0`] up to date!"
	else
		echo "`tput setaf 1 && tput bold`error`tput sgr0`: git pull error"
	fi
	exit
fi

python3 "$HOME/.metamake/tools/metamake.py" "$@"