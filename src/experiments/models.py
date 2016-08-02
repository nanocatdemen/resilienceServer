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
    number_of_nodes = models.IntegerField()
    number_of_edges = models.IntegerField()
    comparison_method = models.CharField(max_length=200)
    main_differences = models.CharField(max_length=200)
    paper = models.ForeignKey('papers.Paper', on_delete=models.CASCADE)
    network_model = models.ManyToManyField(NetworkModel)
    compared_to_metrics = models.ManyToManyField(Metric)
