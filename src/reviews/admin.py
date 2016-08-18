from django.contrib import admin
from .models import *


class QualityStudyAdmin(admin.ModelAdmin):
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

admin.site.register(QualityStudy, QualityStudyAdmin)
