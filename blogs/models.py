from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
	title = models.CharField(max_length = 200)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)
	date_edit = models.DateTimeField(auto_now = True)
	image = models.ImageField(upload_to = 'images',blank = True)
	owner = models.ForeignKey(User,on_delete = models.DO_NOTHING)

	def __str__(self):
		return self.title



