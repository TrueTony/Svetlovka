from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BookFromLivelib(models.Model):
    # libk = models.ChartField(max_length=200)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # tags = models.TextField() #должен быть список
    tags = models.ManyToManyField(Genre)
    cover = models.CharField(max_length=200)
    rating = models.FloatField()
    description = models.TextField()
    key = models.IntegerField()

    def __str__(self):
        return self.title


class ActualBook(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    notes = models.TextField()
    key = models.IntegerField()

    def __str__(self):
        return self.title

