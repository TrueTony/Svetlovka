from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    # litt_of_book

    def __str__(self):
        return self.name


class BookFromLivelib(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.TextField() #должен быть список
    cover = models.CharField(max_length=200)
    rating = models.IntegerField()
    description = models.TextField()
    key = models.IntegerField()

    def __str__(self):
        return self.title


class BookFromLibrary(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    notes = models.TextField()

    def __str__(self):
        return self.title