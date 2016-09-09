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
    abstract = models.TextField()
    times_cited = models.IntegerField()  # (google scholar index)
    source = models.ForeignKey('Source', blank=True, null=True)
    authors = models.ManyToManyField(Author)
    # topics = models.ManyToManyField(Topic)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        from resiliencemetrics.views import paper_detail
        return reverse('paper_detail', kwargs={ "id": self.id})

class Source(models.Model):
    """
    IEEE, Nature, ScienceDirect.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
