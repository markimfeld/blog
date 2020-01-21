from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
	(0, "Draft"),
	(1, "Publish")
)


class Post(models.Model):
	headline = models.CharField(max_length=200, unique=True)
	slug = models.CharField(max_length=200, unique=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
	body_text = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	mod_date = models.DateTimeField(auto_now=True)
	status = models.IntegerField(choices=STATUS, default=0)


	class Meta:
		ordering = ['-pub_date']

	def __str__(self):
		return self.headline