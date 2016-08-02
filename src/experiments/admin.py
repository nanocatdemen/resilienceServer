from django.contrib import admin
from .models import *

# Register your models here.
class NetworkModelInline(admin.TabularInline):
    model = Experiment.network_model.through

class MetricInline(admin.TabularInline):
    model = Experiment.compared_to_metrics.through

class ExperimentAdmin(admin.ModelAdmin):
    inlines = (NetworkModelInline, MetricInline,)
    exclude = ('network_model', 'compared_to_metrics')
    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
            '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/js/select2.min.js',
            'js/paper_has_metric_select2.js',       # project static folder
            #'app/js/myscript.js',   # app static folder
        )
        css = {
             'all': ('//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/css/select2.min.css',)
        }

admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(NetworkModel)
