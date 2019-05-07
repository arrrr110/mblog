from django.urls import path,re_path

# from django.views import View
from rick.views import IndexView, article,category_list,  category ,ArticleDetailView#,DetailView # ArticleListView , #,category #,CategoryListView, ArticleDetailView,

from . import views

app_name = 'rick'
urlpatterns = [
    # 使用通用视图，将常见的模式抽象化https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial04/
    # path('', ArticleListView.as_view(), name='article-list'),
    
    path('',IndexView.as_view(),name='index'),
    path('<category_name_slug>/', views.category, name='category'),  # New!
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    
    # re_path('(?P<category_name_slug>[\w\-]+)/', ArticleListView.as_view(), name='category'),  # New!
    # 文章详情页面 先放弃使用抽象视图的方法
    # path('<slug:article.category.slug>/<int:pk>/$', views.article ,name='article-detail'),
    # 文章详情页面
    # path('(<category_name_slug>/(?<pk>)/', DetailView.as_view(), name='article'),\\
]