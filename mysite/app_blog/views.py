from django.shortcuts import render
from django.views.generic import ListView, DateDetailView
from .models import Article, Category

class HomePageView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(main_page=True)[:5]
        return context

    def get_queryset(self):
        return Category.objects.all()

class ArticleDetail(DateDetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'item'
    date_field = 'pub_date'
    query_pk_and_slug = True
    month_format = '%m'
    allow_future = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        return context

class ArticleList(ListView):
    model = Article
    template_name = 'articles_list.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.filter(slug=self.kwargs.get('slug')).first()
        return context

class ArticleCategoryList(ArticleList):
    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['slug']).distinct()