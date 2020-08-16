from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.




# def home(request,page=1):
#     articles_list = models.Articles.objects.published()
#     paginator = Paginator(articles_list, 5)
#     articles = paginator.get_page(page)
#     context = {
#     "article": articles
#     }
#     return render(request,"blog/home.html",context)

class ArticleList(ListView):
    queryset = models.Articles.objects.published()
    paginate_by = 3

# def detail(request,slug):
#     context={
#     "article":get_object_or_404(models.Articles,slug=slug)
#     }
#     return render(request,"blog/detail.html",context)

class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(models.Articles,slug=slug)



# def category(request,slug, page=1):
#     category = get_object_or_404(models.Category,slug=slug)
#     articles_list = category.article.published()
#     paginator = Paginator(articles_list,3)
#     articles = paginator.get_page(page)
#     context={
#     "category":category,
#     "articles": articles
#     }
#     return render(request,"blog/category.html",context)

class CategoryList(ListView):
    paginate_by = 5
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(models.Category,slug=slug)
        return category.article.published()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
