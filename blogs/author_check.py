def checking_author(request,post_id):
	post = BlogPost.objects.get(id = post_id)
	if  post.owner != request.user:
		raise Http404