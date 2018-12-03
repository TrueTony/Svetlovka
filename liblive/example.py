import json
from liv.models import BookFromLivelib, Author, ActualBook, Genre


# добавление автора
f = open('list_of_books.txt', 'r')
data = json.load(f)
for book in data:
    for author in book[1]:
        if not Author.objects.filter(name=author).exists():
                a = Author()
                a.name = author
                a.save()
f.close()

# добавление книг из вишлиста
f = open('list_of_books.txt', 'r')
data = json.load(f)
for i in data[:5]:
        b = BookFromLivelib()
        b.title = i[2]
        b.author = Author.objects.get(name=i[1][0])
        # for y in i[3]:
          #       b.tags = Genre.objects.get(name=y)
        b.cover = i[4]
        b.rating = i[5]
        b.description = i[6]
        b.key = i[7]
        b.save()

f.close()

# добавление жанров
f = open('list_of_books.txt', 'r')
data = json.load(f)
for book in data:
        for tag in book[3]:
                if not Genre.objects.filter(name=tag).exists():
                        g = Genre()
                        g.name = tag
                        g.save()
f.close()

# присовение жанров книге
f = open('list_of_books.txt', 'r')
data = json.load(f)
for i in data[:5]:
        b = BookFromLivelib.objects.get(title=i[2])
        for g in i[3]:
                genre = Genre.objects.get(name=g)
                b.tags.add(genre)
        b.save()

# добавление книг из библиотеки
f = open('actual_in_lib.txt', 'r')
data = json.load(f)
for i in data[:5]:
        a = ActualBook()
        a.author = i[0]
        a.title = i[1]
        a.notes = i[2]
        a.key = BookFromLivelib.objects.get(key=i[3])
        a.save()