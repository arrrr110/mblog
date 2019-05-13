from django.urls import path,re_path

# from django.views import View
from rick.views import IndexView, ArticleDetailView, category,CategoryListView, AboutView ,detail #ExampleDetailView

from . import views

app_name = 'rick'
urlpatterns = [
    # 使用通用视图，将常见的模式抽象化https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial04/
    # ex:/index/
    path('<int:id>/',views.detail, name='example'),
    path('',IndexView.as_view(),name='index'),
    # ex:/slug1/
    path('<category_name_slug>/', views.category, name='category'),  # New!
    # ex:/slug1/8/
    path('<category_name_slug>/<int:pk>/', ArticleDetailView.as_view(), name='article'),
    path('about/', views.AboutView, name='about'),
    
 
]