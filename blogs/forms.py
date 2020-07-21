from django import forms

from .models import BlogPost

class BlogPostForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['title']
		labels = {'text':''}

class EditPostForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['text']
		labels = {'text':''}




