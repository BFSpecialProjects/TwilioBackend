#!/bin/bash
# start the python backend, currently proof-of-concept
python twilioPOC.py

# forward localhost
ssh -R 80:127.0.0.1:5000 ssh.localhost.run