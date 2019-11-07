from django.db import models

# Create your models here.

class PostModel(models.Model):
	judul		= models.CharField(max_length=100)
	body		= models.TextField()
	author		= models.CharField(max_length=100)
	
	LIST_CATEGORY	= (
		('Jurnal','Jurnal'),
		('Berita','Berita'),
		('Gosip','Gosip'),
		)

	category	= models.CharField(
		max_length=100,
		choices = LIST_CATEGORY,
		default = 'Jurnal',
		)

	def __str__(self):
		return "{}. {}".format(self.id,self.judul)