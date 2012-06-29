#!/usr/bin/env zsh

if [ -n "$1" ]; then
    OPENBOX="$1"
else 
    OPENBOX=`pwd`
fi

ln -nfs $OPENBOX ~/.config/openbox
ln -nfs $OPENBOX/themes ~/.themes
