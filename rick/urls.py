from django.urls import path,re_path

from . import views

# app_name = 'rick'
urlpatterns = [
    # 使用通用视图，将常见的模式抽象化https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial04/
    path('', views.index, name='index'),
    re_path('(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),  # New!
    # 文章详情页面
    # re_path('(?P<category_name_slug>[\w\-]+)/(?P<slug>.*?)/$', views.DetailView.as_view(), name='article'),
]