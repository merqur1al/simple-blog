from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse 
from django.http import HttpResponseRedirect
from django.contrib.auth import logout,login,authenticate

# Create your views here.

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('users:login'))

def register(request):
	#
	if request.method != 'POST':
		#Registration form
		form = UserCreationForm()
	else:
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			#Выполнение входа и перенаправление на домашнюю страницу
			auth_user = authenticate(username = new_user.username,password = request.POST['password1'])
			login(request,auth_user)
			return HttpResponseRedirect(reverse('blogs:index'))

	context = {'form':form}

	return render(request,'users/register.html',context)
