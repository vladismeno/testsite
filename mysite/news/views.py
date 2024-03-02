from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Categories


def index(request):
    news = News.objects.all()
    categories = Categories.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories,
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Categories.objects.all()
    category = Categories.objects.get(pk=category_id)
    context = {
        'news': news,
        'categories': categories,
        'category': category
    }
    return render(request, template_name='news/category.html', context=context)
