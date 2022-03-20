#!/bin/bash

if [ -f $HOME/.local/bin/metamake ] ; then
	rm $HOME/.local/bin/metamake
elif [ -f usr/bin/metamake ] ; then
	rm usr/bin/metamake
fi
rm -r "$HOME/.metamake"
echo "metamake successfully uninstalled!"
