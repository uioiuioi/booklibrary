from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import View
from .models import Book
from .forms import BookCreateForm



def formfunc(request):
    if request.method == 'POST':
        form = BookCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('list')
    else:
        form = BookCreateForm()
    return render(request, 'form.html', {'form': form})

def listfunc(request):
    posts = Book.objects.all()
    dictionary = []
    for i in posts:
        dictionary.append(i.__dict__)
    dictionary_sorted = sorted(dictionary, key=lambda x:x['rank'])
    print(dictionary_sorted)
    return render(request, 'list.html', {'posts': dictionary_sorted})

def detailfunc(request, pk):
    post = Book.objects.get(pk=pk)
    return render(request, 'detail.html', {'post': post})