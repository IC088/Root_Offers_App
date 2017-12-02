from django.db import models

class Poster(models.Model):
	 Poster_Name = models.CharField(max_length = 250)
	 Poster_Link = models.CharField(max_length = 1250)
	 Poster_type = models.CharField(max_length = 250)
	 Poster_creator = models.CharField(max_length = 250)
