from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Experiment)
admin.site.register(NetworkModel)
admin.site.register(ExperimentHasNetworkModel)
admin.site.register(ExperimentComparedToMetric)
