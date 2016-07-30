from django.db import models


class QualityStudy(models.Model):
    """
    Revision study realized.
    """
    topic_described = models.FloatField()
    metric_described = models.FloatField()
    results_complete = models.FloatField()
    additional_comments = models.CharField(max_length=200)
    paper = models.OneToOneField('papers.Paper', on_delete=models.CASCADE)
