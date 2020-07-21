from django.shortcuts import render 
from django.urls import reverse
from django.http import HttpResponseRedirect,Http404

from .forms import BlogPostForm,EditPostForm
from .models import BlogPost
from django.contrib.auth.decorators import login_required

def check_post_owner(request,owner_id):
	check = BlogPost.objects.get(id = owner_id)
	if  check.owner != request.user:
		raise Http404

def index(request):
	return render(request,'blogs/index.html')


def posts(request):
	posts = BlogPost.objects.order_by('-date_added')
	context = {'posts':posts}
	return render (request,'blogs/posts.html',context)


def post(request,post_id):
	post = BlogPost.objects.get(id = post_id)
	post_text = post.text
	username = post.owner
	context = {'post':post,'post_text':post_text,'username':username}
	return render (request,'blogs/post.html',context)

@login_required
def add_post(request):
	if request.method !='POST':
		form = BlogPostForm()
	else:
		form = BlogPostForm(request.POST)
		if form.is_valid():
			new_post = form.save(commit = False)
			new_post.owner = request.user
			new_post.save()
			return HttpResponseRedirect(reverse('blogs:posts'))
	context = {'form':form}
	return render (request,'blogs/add_post.html',context)

@login_required
def edit_post(request,post_id):
	post = BlogPost.objects.get(id = post_id)
	post_text = post.text
	title = post.title
	check_post_owner(request,post_id)
	if request.method != 'POST':
		form = EditPostForm(instance = post)
	else:
		form = EditPostForm(instance = post,data = request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blogs:post',args = [post.id]))

	context = {'post':post,'post_text':post_text,'form':form}
	return render (request,'blogs/edit_post.html',context)



