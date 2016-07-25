from django.db import models


class Paper(models.Model):
    doi = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    # publication_year = models.DateTimeField('date published')
    # authors
    abstract = models.CharField(max_length=200)
    # source
    # metrics
    # topic
    # times_cited
    # experiment
    # additional_comments
