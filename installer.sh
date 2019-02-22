#!/bin/bash
echo "Welcome to the NestWatch Installer!\n\n"

# get the latest version of the program (in this case, proof of conecpt ver)
echo "\n\n\n\nGetting the latest version of NestWatch...\n\n\n"

wget https://github.com/BFSpecialProjects/TwilioBackend/blob/master/twilioPOC.py

### install dependencies ###
# pip, if it isn't already installed
echo "\n\n\nInstalling pip, if it isn't already here...\n\n\n"
sudo apt-get install python-pip

# flask
echo "\n\n\nResolving dependencies...\n\n\n"
pip install flask

# twilio api
pip install twilio

# install latest version of launcher
echo "\n\n\nGetting the latest version of the Launcher...\n\n\n"
wget https://github.com/BFSpecialProjects/TwilioBackend/blob/master/launch.sh

echo "\n\n\n\All done! Run ./launch.sh to get started."