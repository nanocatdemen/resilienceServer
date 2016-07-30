from django.db import models

# Create your models here.
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

class NetworkModel(models.Model):
    """
    Network model such as BA, ER, WS.
    """
    name = models.CharField(max_length=200)

class ExperimentHasNetworkModel(models.Model):
    """
    Which network model was used.
    """
    network_model = models.ForeignKey('NetworkModel', on_delete=models.CASCADE)
    experiment = models.ForeignKey('Experiment', on_delete=models.CASCADE)

class ExperimentComparedToMetric(models.Model):
    """
    Which metrics were compared in the experiment.
    """
    metric = models.ForeignKey('resiliencemetrics.Metric', on_delete=models.CASCADE)
    experiment = models.ForeignKey('Experiment', on_delete=models.CASCADE)
