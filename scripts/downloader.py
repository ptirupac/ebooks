import csv
import requests
import os
import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

if os.name == 'nt':
    delimitter = '\\'
else:
    delimitter = '/'

with open('..{0}data{0}redirected_urls.csv'.format(delimitter), newline='') as f:
    reader = csv.reader(f)
    books_list = list(reader)

# books_list --> Python List
# 0 --> Index
# 1 --> BookName
# 2 --> Original URL
# 3 --> Redirected URL

print('Getting Redirected URLS: ')
os.mkdir('..{0}books'.format(delimitter))
for i, book in enumerate(books_list):
    print('{0} : {1}'.format(i, book[1]))
    data = requests.get(book[3].replace('/book/', '/content/pdf/'))
    open('..{0}books{0}{1}.pdf'.format(delimitter, book[1]), 'wb').write(data.content)
