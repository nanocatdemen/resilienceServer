from django.db import models


class Metric(models.Model):
    name = models.CharField(max_length=200)
    definition = models.TextField()
    interpretation = models.TextField()
    paper = models.ManyToManyField('papers.Paper', through='PaperHasMetric')
    application = models.ManyToManyField('Application', blank=True)
    metric_type = models.ManyToManyField('MetricType')
    additional_comments = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Application(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class MetricType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class PaperHasMetric(models.Model):
    paper = models.ForeignKey('papers.Paper', on_delete=models.CASCADE)
    metric = models.ForeignKey('Metric', on_delete=models.CASCADE)
    is_cited = models.BooleanField()
