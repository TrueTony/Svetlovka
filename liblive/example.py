import json
from liv.models import BookFromLivelib, Author


f = open('list_of_books.txt', 'r')
data = json.load(f)
for book in data:
    for author in book[1]:
        a = Author()
        a.name = author
        a.save()
f.close()

f = open('list_of_books.txt', 'r')
data = json.load(f)
for i in data[:5]:
    if len(i[1]) == 1:
        b = BookFromLivelib()
        b.title = i[2]
        for name in i[1]:
            # b.author = name
            b.author = Author.objects.get(name=name)
        b.tags = i[3]
        b.cover = i[4]
        b.rating = i[5]
        b.description = i[6]
        b.key = i[7]
        b.save()
f.close()