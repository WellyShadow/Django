from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.


def news_home(request):
    news = Artiles.objects.order_by('-date')
    return render(request, 'news/news_home.html',{'news':news})

class NewsUpdateView(UpdateView):
    model=Artiles
    template_name='news/create.html'
    
    #fields=['title','announcement','full_text','date']
    form_class = ArtilesForm

class NewsDeleteView(DeleteView):
    model=Artiles
    template_name='news/news_delete.html'
    success_url = '/news/'
    
class NewsDetailView(DetailView):
    model=Artiles
    template_name='news/detail_view.html'
    context_object_name = 'article'

def create(request):
    error=''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Error Form'

    form = ArtilesForm()
    data ={
        'form':form,
        'error':error
    }
    return render(request,'news/create.html',data)
