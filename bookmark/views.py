from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Bookmark
# in this app, every view will be made with class style view. not function style.
class BookmarkListView(ListView): # ListView를 상속해서 사용한다
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView): # import한 UpdateView를 상속받도록 BookmarkUpdateView를 만든다.
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6 # 한 페이지에 몇 개씩 출력할 것인지 결정하는 값