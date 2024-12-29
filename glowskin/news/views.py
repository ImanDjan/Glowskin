from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from .forms import UserRegistrateForm

from django.views.generic import DetailView


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_file.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_file')
        else:
            error = 'Форма заполнена неверно'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)


def reg(request):
    error = ''
    if request.method == 'POST':
        form = UserRegistrateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_file')
        else:
            error = 'Форма заполнена неверно'
    form = UserRegistrateForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/reg_user.html', data)

