from django.db import models
from resiliencemetrics.models import Metric

# Create your models here.
class NetworkModel(models.Model):
    """
    Network model such as BA, ER, WS.
    """
    name = models.CharField(max_length=200)

class Experiment(models.Model):
    """
    Experiment done in the article
    """
    is_real = models.BooleanField()
    number_of_nodes = models.IntegerField(blank=True, null=True)
    number_of_edges = models.IntegerField(blank=True, null=True)
    comparison_method = models.TextField()
    main_differences = models.TextField()
    paper = models.ForeignKey('papers.Paper', on_delete=models.CASCADE)
    network_model = models.ManyToManyField(NetworkModel, blank=True)
    compared_to_metrics = models.ManyToManyField(Metric)

    def __str__(self):
        return self.paper.title
