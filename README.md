# Passcheck
Aesthetically pleasing password checker which utilizes the haveibeenpwned api

_Currently only supports csv files_

![Example1](/.resources/examp.png)
![Example2](/.resources/examp2.png)

# Note Regarding Security
All passwords are sha1 hashed. Only first 5 characters of the hash are sent to the api ([haveibeenpwned](https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange) uses [k-anonymity](https://en.wikipedia.org/wiki/K-anonymity)) over HTTPS. The rest of the hash is checked against the hashes returned by the api ([Padding](https://haveibeenpwned.com/API/v3#PwnedPasswordsPadding) option has been enabled)

# Install
Clone this repository

    git clone https://github.com/Wocx32/Passcheck.git

Install the requirements

    pip install -r requirements.txt

or

    pip3 install -r requirements.txt

# Usage

Provide a csv file containing url, username and password columns as commandline argument

    python3 main.py example/example.csv

or

    python main.py example/example.csv



_Note: It has been tested with csv files exported by Chrome, Firefox and Bitwarden_

# Configuration

The specific columns containing the url, username and password can be set in `config.py`

# Requirements
- [Python3](https://www.python.org/)
- [rich](https://github.com/Textualize/rich)