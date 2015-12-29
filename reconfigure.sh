#!/usr/bin/env sh

cd ~/.config/openbox

if [ "$1" = '--debug' ]; then
    ./inner-reconfigure.sh &> debug.txt
else
    ./inner-reconfigure.sh
fi

