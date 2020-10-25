from django.shortcuts import render 
from django.urls import reverse
from django.http import HttpResponseRedirect,Http404


from .forms import BlogPostForm,EditPostForm
from .models import BlogPost
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .decorators import allowed_user
from .author_check import checking_author
from .own_classes import OwnPaginator

def index(request):
	return render(request,'blogs/index.html')


def posts(request):
	posts = BlogPost.objects.order_by('-date_added')[:10]
	context = {'posts':posts}
	return render (request,'blogs/posts.html',context)
 

def post(request,post_id):
	post = BlogPost.objects.get(id = post_id)
	
	#OwnPaginator take 2 args:model name(model_name) and post id(p_id)
	pag = OwnPaginator(BlogPost,post_id)

	next_post = pag.show_next_post()
	previous_post = pag.show_previous_post()

	post_text = post.text
	username = post.owner
	context = {
		'post':post,
		'post_text':post_text,
		'username':username,
		'previous_post':previous_post,
		'next_post':next_post
	}
	return render (request,'blogs/post.html',context)


@login_required
@allowed_user(allowed_roles=['admins'])
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
@allowed_user(allowed_roles=['admins'])
def edit_post(request,post_id):
	post = BlogPost.objects.get(id = post_id)
	post_text = post.text
	title = post.title
	checking_author(request,post_id)
	if request.method != 'POST':
		form = EditPostForm(instance = post)
	else:
		form = EditPostForm(instance = post,data = request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blogs:post',args = [post.id]))

	context = {'post':post,'post_text':post_text,'form':form}
	return render (request,'blogs/edit_post.html',context)




