from django.contrib import admin
from .models import *

class PaperHasMetricInline(admin.TabularInline):
    model = Metric.cited_in.through
    extra = 1 # how many rows to show

class PaperApplicationInline(admin.TabularInline):
    model = Metric.application.through
    extra = 1 # how many rows to show

class PaperMetricTypeInline(admin.TabularInline):
    model = Metric.metric_type.through
    extra = 1 # how many rows to show

class MetricClassAdmin(admin.ModelAdmin):
    inlines = (PaperHasMetricInline, PaperApplicationInline, PaperMetricTypeInline,)
    search_fields = ['name',]
    exclude = ('cited_in', 'application', 'metric_type',)
    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
            '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/js/select2.min.js',
            'js/select2_hack.js',       # project static folder
            #'app/js/myscript.js',   # app static folder
        )
        css = {
             'all': ('//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/css/select2.min.css',)
        }

admin.site.register(Metric, MetricClassAdmin)

# admin.site.register(Metric)
admin.site.register(Application)
admin.site.register(MetricType)
# admin.site.register(PaperHasMetric)
