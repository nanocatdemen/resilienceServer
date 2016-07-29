from django.contrib import admin

from .forms import PaperForm
from .models import Paper

class PaperAdmin(admin.ModelAdmin):
    list_display = ["__str__", "doi"]
    form = PaperForm

admin.site.register(Paper, PaperAdmin)
