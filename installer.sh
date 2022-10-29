#!/bin/bash

path=$(which npm)


node_install(){
    echo "Installing Node"
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.2/install.sh | bash >> /dev/null 2>&1
    sleep 2
    source ~/.nvm/nvm.sh
    source ~/.bashrc
    source ~/.profile
    nvm install node >> /dev/null 2>&1
    echo "Node installed successfully"
    sleep 1
    
}

flood_installer(){
    npm install --global flood >> /dev/null 2>&1
}




# installation process start here

# check if nvm and npm is install or not
if [ -z "$path" ]
then
  node_install  
fi
# install flood
flood_installer

