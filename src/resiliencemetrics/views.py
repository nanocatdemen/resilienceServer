from django.shortcuts import render

from .forms import PaperForm
from papers.models import Paper

def home(request):
    title = 'Welcome'
    form = PaperForm(request.POST or None)

    context = {
        'title': title,
        'form': form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    return render(request, 'home.html', context)

def list_papers(request):
    papers = Paper.objects.all()
    return render(request, 'list_papers.html', locals())
