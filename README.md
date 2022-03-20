# Passcheck
A password checker which utilizes the haveibeenpwned api

_Currently only supports csv files_

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


![Example](/.resources/examp.png)

_Note: It has been tested with csv files exported by Chrome, Firefox and Bitwarden_

# Configuration

The specific columns containing the url, username and password can be set in `config.py`

# Requirements
- [Python3](https://www.python.org/)
- [rich](https://github.com/Textualize/rich)