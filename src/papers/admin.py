from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Paper)
admin.site.register(Topic)
admin.site.register(PaperHasTopic)
admin.site.register(Author)
admin.site.register(PaperHasAuthor)
admin.site.register(Source)
