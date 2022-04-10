import json
import csv

users = []
books = []
users_result = []

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
            users[counter]['books'].append({
            "Title": i['Title'],
            "Author": i['Author'],
            "Genre": i['Genre'],
            "Pages": i['Pages'],
        })
            
            counter += 1
    except KeyError:
        users[counter]['books'] = [{
            "Title": i['Title'],
            "Author": i['Author'],
            "Genre": i['Genre'],
            "Pages": i['Pages'],
        }]
        counter += 1
    except IndexError as e:
        counter = 0
    except Exception as e:
        Exception(f"Непредвиденная ошибка - { e }")

for i in users:
    users_result.append(
        {
            "name": i['name'],
            "gender": i['gender'],
            "address": i['address'],
            "age": i['age'],
            "books": i['books']
        }
    )

with open('./reference.json', 'w') as file:
    json.dump( users_result, file, indent=4 )


