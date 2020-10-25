from django.shortcuts import redirect
from django.http import HttpResponse



def unauthenticated_user(func):
	def wrapper(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('blogs:index')
		else:
			return func(request, *args, **kwargs)
	return wrapper


def allowed_user(allowed_roles=[]):
	def decorator(func):
		def wrapper(request, *args, **kwargs):
			if request.user.groups.filter(name__in=allowed_roles).exists():
				return func(request, *args, **kwargs)
			else:
				return HttpResponse('You do not have enought rights to view it :(')
		return wrapper
	return decorator