from django.urls import path

from . import views

urlpatterns = [
#Home page
path('',views.index,name = 'index'),
#Page with the list of posts
path('posts',views.posts,name = 'posts'),
#Page with details for every post
path('post/<int:post_id>',views.post,name = 'post'),
#Ability that add post
path('add_post',views.add_post,name = 'add_post'),
#Ability to change text of post
path('edit_post/<int:post_id>',views.edit_post,name = 'edit_post')
]

app_name = 'blogs'