from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    born_date = models.CharField(max_length=100)
    born_location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.full_name

    
class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.tag


class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.text[:20]