from django.db import models


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

    def __str__(self):
        return self.title

class Topic(models.Model):
    name = models.CharField(max_length=200)

class PaperHasTopic(models.Model):
    paper = models.ForeignKey('Paper', on_delete=models.CASCADE)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField(max_length=200)

class PaperHasAuthor(models.Model):
    paper = models.ForeignKey('Paper', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

class Source(models.Model):
    """
    IEEE, Nature, ScienceDirect.
    """
    name = models.CharField(max_length=200)
