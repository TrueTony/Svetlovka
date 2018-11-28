import json
from liv.models import BookFromLivelib, Author, ActualBook, Genre


f = open('list_of_books.txt', 'r')
data = json.load(f)
for book in data:
    for author in book[1]:
        if not Author.objects.filter(name=author).exists():
                a = Author()
                a.name = author
                a.save()
f.close()

f = open('list_of_books.txt', 'r')
data = json.load(f)
for book in data:
        for tag in book[3]:
                if not Genre.objects.filter(name=tag).exists():
                        g = Genre()
                        g.name = tag
                        g.save()
f.close()

f = open('list_of_books.txt', 'r')
data = json.load(f)
for i in data:
        b = BookFromLivelib()
        b.title = i[2]
        b.author = Author.objects.get(name=i[1][0])
        for y in i[3]:
                b.tags = Genre.objects.get(name=y)
        b.cover = i[4]
        b.rating = i[5]
        b.description = i[6]
        b.key = i[7]
        b.save()

f.close()

f = open('actual_in_lib.txt', 'r')
data = json.load(f)
for i in data:
        c = ActualBook()
        c.author = i[0]
        c.title = i[1]
        c.notes = i[2]
        c.key = i[3]
        c.save()