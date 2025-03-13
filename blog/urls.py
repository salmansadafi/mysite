from django.urls import path
from blog.views import *

app_name="blog"
urlpatterns = [
    path('',blog_view,name="index"),
    path('single',blog_single_view,name="single"),
    path('post-<int:pid>',test,name="test"),
    path('<int:post_id>',blog_detail,name="detail"),
    
]