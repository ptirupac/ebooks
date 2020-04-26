import csv
import requests
import os
import sys


if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

# Getting current file's full path
dir_path = os.path.dirname(os.path.realpath(__file__))

if os.name == 'nt':
    delimitter = '\\'
else:
    delimitter = '/'

with open('{0}{1}..{1}data{1}redirected_urls.csv'.format(dir_path, delimitter), newline='') as f:
    reader = csv.reader(f)
    books_list = list(reader)

# books_list --> Python List
# 0 --> Index
# 1 --> BookName
# 2 --> Original URL
# 3 --> Redirected URL

# Creating ../books directory
try:
    books_path = '{0}{1}..{1}books'.format(dir_path, delimitter)
    os.mkdir(books_path)
    print('Created books directory @ : {0}'.format(books_path))
except Exception:
    print('Books directory @ : {0}'.format(books_path))

print('\nGetting Redirected URLS: \n')


for i, book in enumerate(books_list):
    print('{0} : {1}'.format(i, book[1]))
    data = requests.get(book[3].replace('/book/', '/content/pdf/'))
    open('{0}{1}..{1}books{1}{2}.pdf'.format(dir_path, delimitter, book[1]), 'wb').write(data.content)

print('\n \n ~~~~~~~~~ https://ptirupac.com ~~~~~~~~~')
