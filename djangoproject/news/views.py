from django.shortcuts import render
from .models import Artiles
# Create your views here.
def news_home(request):
    news = Artiles.objects.order_by('-date')
    return render(request, 'news/news_home.html',{'news':news})
def create(request):
    return render(request,'news/create.html')
