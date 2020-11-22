#!/bin/bash

mkdir -p $HOME/.personalizar-alias/src/
cp -rv src $HOME/.personalizar-alias/
cp -rv main.py $HOME/.personalizar-alias/

sudo cp -v src/local/personalizar-alias /usr/local/bin
sudo chmod +x /usr/local/bin/personalizar-alias