from django.shortcuts import render

from .forms import PaperForm
from papers.models import Paper
from .models import Metric

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

def list_metrics(request):
    metrics = Metric.objects.all()
    return render(request, 'list_metrics.html', locals())

def show_metric(request, id=None):
    metric = Metric.objects.get(id=id)
    return render(request, 'show_metric.html', locals())

def show_paper(request, id=None):
    paper = Paper.objects.get(id=id)
    return render(request, 'show_paper.html', locals())
