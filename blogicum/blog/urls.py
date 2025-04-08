from django.urls import path
from django.shortcuts import render 
from .views import index, post_detail, category_view, about, rules
from django.conf import settings
from django.conf.urls.static import static



app_name = "blog"


urlpatterns = [
    path('', index, name='index'),  
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', category_view, name='category'),
    path('about/', about, name='about'), 
    path('rules/', rules, name='rules'), 
    path('detail/', rules, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

