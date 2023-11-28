from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views import View
from .models import News, Category, Tag
from django.urls import reverse_lazy
from .forms import AddNewsForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from hitcount.views import HitCountDetailView
from django.utils.text import slugify
from hitcount.models import HitCount

# Create your views here.

class HomePage(ListView):
    template_name = 'index.html'
    model = News

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        category_list = Category.objects.all()
        hit_top_news = HitCount.objects.order_by('-hits')

        top_news = []
        for x in hit_top_news:
            top_news.append(x.content_object)
        #top_news = News.objects.order_by("-view_co")
        last_news = News.objects.order_by("-update_at")
        tag_list = Tag.objects.all()

        last = last_news[0]
        top = top_news[0]
        last_news = last_news[1:]
        if len(last_news) > 8:
            last_news = last_news[1:8]

        top_news = top_news[1:]
        if len(top_news) > 5:
            top_news = top_news[1:5]
        
        newscate = []

        for cate in category_list:
            l = []
            l.append(cate)
            cate_list = cate.news.order_by('-create_at')
            cate_elements = 3 # count of elements to show in banner
            if len(cate_list) > cate_elements:
                cate_list = cate_list[:cate_elements]

            for y in cate_list:
                l.append(y)
            newscate.append(l)        
        
        context['top_news'] = top_news
        context['top'] = top
        context['newscate'] = newscate
        context['category_list'] = category_list
        context['tag_list'] = tag_list
        context['last'] = last
        context['last_news'] = last_news
        return context

class SearchView(ListView):
    template_name = 'listview.html'
    model = News


    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("search")
        context['query'] = query
        object_list = News.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        context['title'] = f"Search: '{query}' results:"
        context['news'] = object_list
        return context

class CategoryView(ListView):
    template_name = 'listview.html'
    model = News

    def get(self, request, name) -> HttpResponse:
        context = {}
        category = Category.objects.get(name_en = name)
        context['title'] = f"{category.name}"
        context['news'] = category.news.all()
        return render(request, self.template_name, context)
        
class MyNewsView(ListView):
    template_name = 'listview.html'
    model = News

    def get(self, request) -> HttpResponse:
        context = {}
        context['title'] = f"{request.user}"
        context['news'] = News.objects.filter(user_id=request.user)
        return render(request, self.template_name, context)
        
class TagsView(ListView):
    template_name = 'listview.html'
    model = News

    def get(self, request, pk) -> HttpResponse:
        context = {}
        tag = Tag.objects.get(id=pk)
        context['title'] = f"{tag.name}"
        context['news'] = tag.news.all()
        return render(request, self.template_name, context)
        
class AuthorView(ListView):
    template_name = 'listview.html'
    model = News

    def get(self, request, slug) -> HttpResponse:
        context = {}
        user = User.objects.get(username=slug)
        context['title'] = f"{user.username}"
        context['news'] = user.news.all()
        return render(request, self.template_name, context)

class AddNewsView(LoginRequiredMixin, CreateView):
    model = News
    form_class = AddNewsForm
    template_name = 'add_new.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        form.instance.slug = slugify(form.cleaned_data['title'])
        return super().form_valid(form)
    
class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    form_class = AddNewsForm
    template_name = 'add_new.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        new = self.get_object()
        if self.request.user == new.user_id or self.request.user.is_superuser:
            return True
        return False

class DeleteNewsView(DeleteView):
    model = News
    success_url = reverse_lazy('home')

    def test_func(self):
        new = self.get_object()
        if self.request.user == new.user_id or self.request.user.is_superuser:
            return True
        return False

class DetailView(HitCountDetailView):
    model = News
    template_name = 'detail.html'
    count_hit = True


    



    
