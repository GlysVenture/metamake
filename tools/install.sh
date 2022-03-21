#!/bin/bash

#check if .metamake dir already exists
if [ -d $HOME/.metamake ]; then
	echo "`tput setaf 1 && tput bold`error`tput sgr0`:"' $HOME/.metamake already exists. update metamake with --update'
	exit 1
else
	cp -r . $HOME/.metamake
fi

#tries to setup smbolic link in users PATH, usually in $HOME/.local/bin if it exists
if [ -d $HOME/.local/bin ]; then
	ln -s $HOME/.metamake/metamake.sh $HOME/.local/bin/metamake
	echo "[`tput setaf 6 && tput bold`metamake`tput sgr0`]"' installed in $HOME/.local/bin/metamake -> $HOME/.metamake/metamake.sh'
elif mkdir /usr/bin/metamake; then
    rmdir /usr/bin/metamake
    ln -s $HOME/.metamake/metamake.sh usr/bin/metamake
    echo "[`tput setaf 6 && tput bold`metamake`tput sgr0`]"' installed in usr/bin/metamake -> $HOME/.metamake/metamake.sh'
else
	echo "`tput setaf 1 && tput bold`error`tput sgr0`: couldn't create symlink. installation cancelled"
	rm -r $HOME/.metamake
	exit 1
fi
