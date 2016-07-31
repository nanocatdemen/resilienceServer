from django.db import models


class Metric(models.Model):
    name = models.CharField(max_length=200)
    definition = models.CharField(max_length=200)
    interpretation = models.CharField(max_length=200)
    paper = models.ManyToManyField('papers.Paper', through='PaperHasMetric')
    application = models.ManyToManyField('Application')
    metric_type = models.ManyToManyField('MetricType')

class Application(models.Model):
    name = models.CharField(max_length=200)

class MetricType(models.Model):
    name = models.CharField(max_length=200)

class PaperHasMetric(models.Model):
    paper = models.ForeignKey('papers.Paper', on_delete=models.CASCADE)
    metric = models.ForeignKey('Metric', on_delete=models.CASCADE)
    is_cited = models.BooleanField()
