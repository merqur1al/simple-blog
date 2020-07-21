from django.urls import path

from . import views

urlpatterns = [
path('',views.index,name = 'index'),
path('posts',views.posts,name = 'posts'),
path('post/<int:post_id>',views.post,name = 'post'),
path('add_post',views.add_post,name = 'add_post'),
path('edit_post/<int:post_id>',views.edit_post,name = 'edit_post')
]

app_name = 'blogs'