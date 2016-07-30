from django.contrib import admin
from .models import *


admin.site.register(Metric)
admin.site.register(Application)
admin.site.register(MetricHasApplication)
admin.site.register(MetricType)
admin.site.register(MetricsHasType)
admin.site.register(PaperHasMetric)
