import json
from liv.models import BookFromLivelib, Author


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
for i in data:
        b = BookFromLivelib()
        b.title = i[2]
        b.author = Author.objects.get(name=i[1][0])
        b.tags = i[3]
        b.cover = i[4]
        b.rating = i[5]
        b.description = i[6]
        b.key = i[7]
        b.save()
        
f.close()