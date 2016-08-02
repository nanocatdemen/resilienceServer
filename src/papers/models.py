from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# class Topic(models.Model):
#     name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name

class Paper(models.Model):
    """
    Science article.
    """
    doi = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    abstract = models.CharField(max_length=200)
    times_cited = models.IntegerField()  # (google scholar index)
    source = models.ForeignKey('Source', blank=True, null=True)
    authors = models.ManyToManyField(Author)
    # topics = models.ManyToManyField(Topic)

    def __str__(self):
        return self.title

class Source(models.Model):
    """
    IEEE, Nature, ScienceDirect.
    """
    name = models.CharField(max_length=200)
