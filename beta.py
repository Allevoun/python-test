import requests
from getpass import getpass
username = 'Allevoun'
password = 'git701927levon'
r = requests.get('https://api.github.com/user', auth=(username, password))
print(r.text)

