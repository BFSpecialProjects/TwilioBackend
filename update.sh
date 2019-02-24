# update NestWatch
echo "Upgrading to the Latest Version of NestWatch...\n\n"

# remove old version
rm ~/NestWatchServer/PythonBackend/TwilioBackend/NestWatch.py

# install latest version
wget https://raw.githubusercontent.com/BFSpecialProjects/TwilioBackend/master/NestWatch.py

echo "\n\nNestWatch has been updated."