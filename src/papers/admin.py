from django.contrib import admin
from django import forms

# Register your models here.
from .models import *

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']

class AuthorInline(admin.TabularInline):
    model = Paper.authors.through
    search_fields = ['name',]

class TopicInline(admin.TabularInline):
    model = Paper.topics.through

class PaperAdmin(admin.ModelAdmin):
    inlines = (AuthorInline, TopicInline)
    search_fields = ['title',]
    exclude = ('authors', 'topics')
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


admin.site.register(Paper, PaperAdmin)
admin.site.register(Topic)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Source)
