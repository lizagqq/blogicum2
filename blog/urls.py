from django.urls import path
from django.shortcuts import render 
from .views import index, post_detail, category_posts, about, rules
from django.conf import settings
from django.conf.urls.static import static



app_name = "blog"


urlpatterns = [
    path('', index, name='index'),  
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('category/<slug:slug>/', category_posts, name='category_posts'),
    path('about/', about, name='about'), 
    path('rules/', rules, name='rules'), 
    path('detail/', rules, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

