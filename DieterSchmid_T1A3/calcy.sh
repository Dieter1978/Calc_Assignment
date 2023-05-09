#!/bin/bash
if ! [[ -x "$(command -v python)" ]]
then
  echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1
fi
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 /Users/dieterschmid/projects/python/Assignment/DieterSchmid_T1A3/main.py
