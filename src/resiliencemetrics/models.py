from django.db import models
from papers.models import Paper

class Metric(models.Model):
    name = models.CharField(max_length=200)
    definition = models.TextField(blank=True)
    interpretation = models.TextField(blank=True)
    proposed_in = models.ForeignKey('papers.Paper', on_delete=models.CASCADE, related_name='paper_proposed_in', blank=True, null=True)
    cited_in = models.ManyToManyField(Paper, blank=True)
    application = models.ManyToManyField('Application', blank=True)
    metric_type = models.ManyToManyField('MetricType', blank=True)
    additional_comments = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('metric_detail', kwargs={ 'id': self.id})

class Application(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class MetricType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# class PaperHasMetric(models.Model):
#     paper = models.ForeignKey('papers.Paper', on_delete=models.CASCADE)
#     metric = models.ForeignKey('Metric', on_delete=models.CASCADE)
#     is_cited = models.BooleanField()
