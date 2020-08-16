from django.urls import path, re_path
from . import views

app_name = "blog"
urlpatterns = [
    re_path(r'^$', views.ArticleList.as_view(),name="home"),
    re_path(r'^page/(?P<page>\d+)/$', views.ArticleList.as_view(), name="home"),
    re_path(r'^articles/(?P<slug>[-\w]+)/$', views.ArticleDetail.as_view(), name='detail'),
    re_path(r'^category/(?P<slug>[-\w]+)/$', views.CategoryList.as_view(), name='category'),
    re_path(r'^category/(?P<slug>[-\w]+)/page/(?P<page>\d+)/$', views.CategoryList.as_view(), name='category'),
]
