import csv
import requests

with open('../data/ebooks.csv', newline='') as f:
    reader = csv.reader(f)
    books_list = list(reader)

# books_list --> Python List
# 0 --> Index
# 1 --> BookName
# 2 --> Original URL
# 3 --> Redirected URL
# for i, book in enumerate(books_list):

print('Getting Redirected URLS: ')
for i, book in enumerate(books_list):
    print('{0} : {1}'.format(i, book[1]))
    redirected_url = requests.get(book[2])
    book.append(redirected_url.url)


with open("../data/redirected_urls.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(books_list)
