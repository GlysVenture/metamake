#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "`tput setaf 1 && tput bold`error`tput sgr0`: illegal number of parameters"
    exit 1
fi

if [ $1 = --update ] ; then
	git -C $HOME/.metamake restore $HOME/.metamake > /dev/null
	if git -C $HOME/.metamake pull > /dev/null ; then
		echo "[`tput setaf 6 && tput bold`metamake`tput sgr0`] up to date!"
	else
		echo "`tput setaf 1 && tput bold`error`tput sgr0`: git pull error"
	fi
	exit
fi

if [ -z "$(ls -A .)" ]; then
   python3 "$HOME/.metamake/metamake.py" $1
else
   echo "`tput setaf 1 && tput bold`error`tput sgr0`: directory not empty"
fi
