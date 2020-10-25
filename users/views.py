from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse 
from django.http import HttpResponseRedirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import Group

from blogs.decorators import unauthenticated_user
# Create your views here.

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('users:login'))

@unauthenticated_user
def register(request):
	#Creating a registration page
	if request.method != 'POST':
		#Registration form
		form = UserCreationForm()
	else:
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()

			group = Group.objects.get(name='customer')
			new_user.groups.add(group)

			#Redirect to homepage
			auth_user = authenticate(username = new_user.username,password = request.POST['password1'])
			login(request,auth_user)
			return HttpResponseRedirect(reverse('blogs:index'))

	context = {'form':form}

	return render(request,'users/register.html',context)
