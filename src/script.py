import json
import csv

users = []
books = []

with open('./users.json', 'r', newline='' ) as  file:
    users = json.load(file)

with open('./report.csv', 'r') as file:
    reader = csv.reader( file )
    header = next( reader )
    for row in reader:
        books.append( dict( zip( header, row )))

counter = 0
for i in books:
    try:
        if users[counter]['books']:
            users[counter]['books'].append(i)
            counter += 1
    except KeyError:
        users[counter]['books'] = [i]
        counter += 1
    except IndexError as e:
        counter = 0
    except Exception as e:
        Exception(f"Непредвиденная ошибка - { e }")

with open('./reference.json', 'w') as file:
    json.dump( users, file, indent=4 )

# Проверка
with open('./reference.json', 'r') as file:
    reference = json.load(file)
    for user_books in reference:
        print(user_books['books'])