from django.shortcuts import render

from .forms import PaperForm


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
        context = {
            'title': 'yay'
        }
    return render(request, 'home.html', context)