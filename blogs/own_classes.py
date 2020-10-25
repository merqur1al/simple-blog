class OwnPaginator():
	#Return previous and next page
	def __init__(self,model_name,p_id):
		self.model_name = model_name
		self.posts = model_name.objects.all()
		self.post_id = p_id

	def show_next_post(self):
		#FINDING NEXT POST
		posts_id = []
		for p in self.posts:
			posts_id.append(p.id)
		
		if self.post_id == posts_id[-1]:
			next_post = None
		else:
			index_post_id = posts_id.index(self.post_id)
			next_id = posts_id[index_post_id + 1]
			next_post = self.model_name.objects.get(id = next_id)
		
		return next_post

	def show_previous_post(self):
		#FINDING PREVIOUS POST 
		posts_id = []
		for p in self.posts:
			posts_id.append(p.id)

		if self.post_id == posts_id[0]:
			previous_post = None
		else:
			index_post_id = posts_id.index(posts_id)
			previous_id = posts_id[index_post_id - 1]
			previous_post = self.model_name.objects.get(id = previous_id)

		return previous_post