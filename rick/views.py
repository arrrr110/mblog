from django.shortcuts import render
from django.http import HttpResponse
from rick.models import Category, Article
from django.views import generic # 通用视图
from datetime import datetime


def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Category.objects.all()
    context_dict = {'categories': category_list}

    # Render the response and send it back!
    return render(request, 'rick/index.html', context_dict)

# class IndexView(generic.ListView):
#     """
#         首页视图,继承自ListView，用于展示从数据库中获取的文章列表
#     """
#     # 获取数据库中的文章列表
#     model = Category
#     # template_name属性用于指定使用哪个模板进行渲染
#     template_name = 'rick/index.html'
#     # context_object_name属性用于给上下文变量取名（在模板中使用该名字）
#     context_object_name = 'category'

#     paginate_by = 10
    
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Article.objects.order_by()[:15]

class DetailView(generic.DetailView):
    """
        Django有基于类的视图DetailView,用于显示一个对象的详情页，我们继承它
    """
    # 获取数据库中的文章列表
    model = Article
    # template_name属性用于指定使用哪个模板进行渲染
    template_name = 'rick/article.html'
    # context_object_name属性用于给上下文变量取名（在模板中使用该名字）
    context_object_name = 'article'


def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

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
    return render(request, 'rick/category.html', context_dict)