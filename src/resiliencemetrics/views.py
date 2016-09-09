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

def paper_detail(request, id=None):
    paper = Paper.objects.get(id=id)
    return render(request, 'paper_detail.html', locals())

def metric_detail(request, id=None):
    metric = Metric.objects.get(id=id)
    return render(request, 'metric_detail.html', locals())

def viz_metrics(request):
    metrics = Metric.objects.all()
    return render(request, 'viz.html', locals())
