from time import sleep
from config import url_column, username_column, password_column
import requests
import hashlib
import csv
from rich.progress import track
import sys


def request_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url, headers={'Add-Padding': 'true'})
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check api and try again.")
    return res

def get_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_data(first5_char)
    return get_leak_count(response, tail)

def main(file):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        entries = -1  # first row not included
        for row in reader:
            entries += 1

    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        url_index = None
        username_index = None
        password_index = None

        for row in reader:

            try:
                if all((url_column, username_column, password_column)):
                    url_index = row.index(url_column)
                    username_index = row.index(username_column)
                    password_index = row.index(password_column)
                    break

            except ValueError:
                sys.exit("Csv file doesn't contain the required columns") 

            # for Chrome and Firefox
            try:
                url_index = row.index('url')
                username_index = row.index('username')
                password_index = row.index('password')
                break
            except ValueError:
                pass
                

            # for bitwarden
            try:
                url_index = row.index('login_uri')
                username_index = row.index('login_username')
                password_index = row.index('login_password')
                break

            except ValueError:
                sys.exit("Csv file doesn't contain the required columns")


        for row in track(reader, description="Processing...", total=entries):
            result = pwned_api_check(row[password_index])

            print(f"Password for user: {row[username_index]}, on site: {row[url_index]}, appeared {result} times")
            sleep(1.5)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("No file provided")

    sys.exit(main(sys.argv[1]))