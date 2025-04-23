from django.contrib import admin
from .models import Article, ArticleImage, Category
from .forms import ArticleImageForm

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageInline]
    list_display = ('title', 'pub_date', 'category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')

# Реєстрація ArticleImage не потрібна, бо вже є в ArticleAdmin через Inline