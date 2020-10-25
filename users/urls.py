from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from blogs.decorators import unauthenticated_user

urlpatterns = [ 
#Login page
path('login', unauthenticated_user(LoginView.as_view(template_name = 'users/login.html')),name = 'login'),
#Logout page
path('logout',views.logout_view, name = 'logout'),
#Sign up page
path('register',views.register,name = 'register'),
]

app_name = 'users'