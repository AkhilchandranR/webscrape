from django.db import models

class category(models.Model):
	name=models.CharField(max_length=50)
	
	def __str__(self):
		return str(self.id)
	

class newsfeed(models.Model):
	headline=models.CharField(max_length=100)
	author=models.CharField(max_length=50,default='n/a')
	content=models.TextField()
	date=models.DateTimeField(auto_now_add=True)
	catg=models.CharField(max_length=50,null=True)
	image=models.ImageField(null=True,blank=True)
	@property
	def imageURL(self):
		try:
			url=self.image.url
		except:
			url=' '
		return url
	@property
	def noofcomms(self):
		return comment.objects.filter(post=self).count()
	
	def __str__(self):
		return self.headline

class comment(models.Model):
	post=models.ForeignKey(newsfeed,on_delete=models.CASCADE)
	name=models.CharField(max_length=50)
	body=models.TextField()
	class Meta:
		db_table="comment"
	
	def __str__(self):
		return self.name