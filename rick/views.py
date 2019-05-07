from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Category, Article, Tag, Keyword
# from django.views import generic # 通用视图
from django.urls import reverse
from .models import Category, Article
from django.views.generic import ListView, DetailView
from django.utils import timezone
from datetime import datetime

class IndexView(ListView):
    # 获取数据库中的文章列表
    model = Article
    # template_name属性用于指定使用哪个模板进行渲染
    template_name = 'rick/index.html'
    # context_object_name属性用于给上下文变量取名（在模板中使用该名字）
    context_object_name = 'articles'


    """Django 能够为 context 变量决定一个合适的名字。然而对于 ListView， 自动生成的 context 变量是 question_list。为了覆盖这个行为，我们提供 context_object_name 属性，表示我们想使用 latest_question_list。作为一种替换方案，你可以改变你的模板来匹配新的 context 变量 —— 这是一种更便捷的方法，告诉 Django 使用你想使用的变量名。
    # context_object_name = 'latest_question_list' """

    def get_queryset(self):
        """Return the last five published questions."""
        return Article.objects.order_by('-create_date')[:4]


class ArticleDetailView(DetailView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def category_list(request, category):
    try:
        category_post = Article.objects.filter(category__name__iexact=category)
    except article.DoesNotExist:
        raise Http404
    return render(request, 'category_list.html', {"category_post": category_post})

# 文章详情页
def article(request, article_id):
    pass
    # article = get_object_or_404(Article, pk=article_id)
    # return render(request, 'rick/detail.html', {'article': article})

# # 无法取得数据，先放一放
# class ArticleDetailView(DetailView):
#     # 获取数据库中的文章列表
#     model = Article
#     template_name = 'rick/article_detail.html' 
#     # # template_name属性用于指定使用哪个模板进行渲染
#     # template_name = 'rick/article_detail.html'
#     context_object_name = 'object'
#     # pk_url_kwarg ="pk"
#     # 在 get_context_data() 函数中可以用于传递一些额外的内容到网页
#     def get_context_data(self, **kwargs):
#         context = super(ArticleDetailView,self).get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         print('*'*100,context)
#         return context

# class DetailView(DetailView):
#     """
#         Django有基于类的视图DetailView,用于显示一个对象的详情页，我们继承它
#     """
#     # 获取数据库中的文章列表
#     model = Article
#     # template_name属性用于指定使用哪个模板进行渲染
#     template_name = 'article.html'
#     # context_object_name属性用于给上下文变量取名（在模板中使用该名字）
#     context_object_name = 'article'

#     def get_context_data(self, **kwargs):
#         context = super(DetailView, self).get_context_data(**kwargs)
#         context['category'] = self.object.id
#         return context


# 先把这个代码关起来：
'''cats.html：
< a href="{% url 'category' c.slug %}" class="btn btn-lg btn-outline"></ a>
'''
def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}
    print('%'*100)
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        articles = Article.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['article'] = articles
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
        context_dict['category_name_slug'] = category_name_slug
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'rick/category_list.html', context_dict)
