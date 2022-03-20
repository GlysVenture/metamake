#!/bin/bash

mkdir "$HOME/.metamake"
cp metamake.sh $HOME/.metamake/.
cp metamake.py $HOME/.metamake/.
cp -r templates $HOME/.metamake/.
cp -r criterion* $HOME/.metamake/.

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