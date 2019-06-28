#!/bin/bash
echo "Welcome to the NestWatch Installer!\n\n"

### install dependencies ###
# pip, if it isn't already installed
echo "\n\n\nInstalling pip, if it isn't already here...\n\n\n"
sudo apt-get install python-pip

# flask
echo "\n\n\nResolving dependencies...\n\n\n"
pip install flask

# twilio api
pip install twilio

# postgres
psycopg2

# install latest version of launcher
echo "\n\n\nGetting the latest version of the Launcher...\n\n\n"
wget https://github.com/BFSpecialProjects/TwilioBackend/blob/master/launch.sh

echo "\n\n\nAll done!"
