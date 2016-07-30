from django.db import models


class Metric(models.Model):
    name = models.CharField(max_length=200)
    definition = models.CharField(max_length=200)
    interpretation = models.CharField(max_length=200)

class Application(models.Model):
    name = models.CharField(max_length=200)

class MetricHasApplication(models.Model):
    metric = models.ForeignKey('Metric', on_delete=models.CASCADE)
    application = models.ForeignKey('Application', on_delete=models.CASCADE)

class MetricType(models.Model):
    name = models.CharField(max_length=200)

class MetricsHasType(models.Model):
    metric = models.ForeignKey('Metric', on_delete=models.CASCADE)
    metric_type = models.ForeignKey('MetricType', on_delete=models.CASCADE)

class PaperHasMetric(models.Model):
    paper = models.ForeignKey('papers.Paper', on_delete=models.CASCADE)
    metric = models.ForeignKey('Metric', on_delete=models.CASCADE)
    is_cited = models.BooleanField()
