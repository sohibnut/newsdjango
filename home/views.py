from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from .models import News, Category, Tag
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import AddNewsForm
from django.db.models import Q
# Create your views here.

class HomePage(ListView):
    template_name = 'index.html'
    model = News

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        category_list = Category.objects.all()
        tag_list = Tag.objects.all()
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
        

        context['newscate'] = newscate
        context['category_list'] = category_list
        context['tag_list'] = tag_list
        return context

class SearchView(ListView):
    template_name = 'searchview.html'
    model = News

    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('search')
        print(query)
        object_list = News.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        print(object_list)
        return object_list
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get("search")
        return context

class CategoryView(ListView):
    template_name = 'listview.html'
    model = News

    def get(self, request, pk) -> HttpResponse:
        context = {}
        category = Category.objects.get(id=pk)
        context['title'] = category.name
        context['news'] = category.news.all()
        return render(request, self.template_name, context)
        


class Contact():
    pass

@login_required
def addnewsview(request):
    if request.POST:
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_id = request.user
            form.save()
            return redirect('home')
        else:
            print(form.errors)

    context = {}
    context['form'] = AddNewsForm()
    return render(request, 'add_new.html', context)

class DetailView(View):
    template_name = 'detail.html'
    def get(self, request, pk):
        context = {}
        new = News.objects.get(id=pk)
        recom = News.objects.filter(category_id = new.category_id)

        context['recom'] = recom
        context['title'] = new.title
        context['new'] = new
        return render(request, self.template_name, context)

    
