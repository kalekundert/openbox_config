#!/usr/bin/env sh

cd ~/.config/openbox

env > reconfigure.env
./inner-reconfigure.sh &> reconfigure.log
