from django.contrib import admin
from .models import *

class PaperHasMetricInline(admin.TabularInline):
    model = PaperHasMetric
    extra = 2 # how many rows to show

class MetricClassAdmin(admin.ModelAdmin):
    inlines = (PaperHasMetricInline,)
    search_fields = ['title',]
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

admin.site.register(Metric, MetricClassAdmin)

# admin.site.register(Metric)
admin.site.register(Application)
admin.site.register(MetricType)
# admin.site.register(PaperHasMetric)
