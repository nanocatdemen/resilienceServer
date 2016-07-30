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

class Experiment(models.Model):
    """
    Experiment done in the article
    """
    is_real = models.BooleanField()
    number_of_nodes = models.IntegerField()
    number_of_edges = models.IntegerField()
    comparison_method = models.CharField(max_length=200)
    main_differences = models.CharField(max_length=200)
    paper = models.ForeignKey('Paper', on_delete=models.CASCADE)

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
    metric = models.ForeignKey('Metric', on_delete=models.CASCADE)
    experiment = models.ForeignKey('Experiment', on_delete=models.CASCADE)

class QualityStudy(models.Model):
    """
    Revision study realized.
    """
    topic_described = models.FloatField()
    metric_described = models.FloatField()
    results_complete = models.FloatField()
    additional_comments = models.CharField(max_length=200)
    paper = models.OneToOneField(Paper, on_delete=models.CASCADE)

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
    paper = models.ForeignKey('Paper', on_delete=models.CASCADE)
    metric = models.ForeignKey('Metric', on_delete=models.CASCADE)
    is_cited = models.BooleanField()
