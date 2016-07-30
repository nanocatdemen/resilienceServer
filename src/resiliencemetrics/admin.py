from django.contrib import admin

# from .forms import PaperForm
from .models import *


admin.site.register(Paper)
admin.site.register(Experiment)
admin.site.register(Metric)
admin.site.register(Source)
admin.site.register(NetworkModel)
admin.site.register(QualityStudy)
admin.site.register(ExperimentHasNetworkModel)
admin.site.register(ExperimentComparedToMetric)
admin.site.register(Application)
admin.site.register(MetricHasApplication)
admin.site.register(MetricType)
admin.site.register(MetricsHasType)
admin.site.register(PaperHasMetric)
admin.site.register(Topic)
admin.site.register(PaperHasTopic)
admin.site.register(Author)
admin.site.register(PaperHasAuthor)
