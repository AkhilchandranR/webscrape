from django.shortcuts import render,redirect
from .models import *
from feeds.forms import commentform
def index(request):
	feeds=newsfeed.objects.all()
	context={'feeds':feeds}
	return render(request,'feeds.html',context)
	
def View(request,id):
	feeds=newsfeed.objects.get(id=id)
	comments=comment.objects.filter(post=feeds)
	context={'feeds':feeds,'comments':comments}
	return render(request,'view.html',context)
	
def cats(request,catg):
	feeds=newsfeed.objects.filter(catg=catg)
	context={'feeds':feeds}
	return render(request,'category.html',context)

def addcomment(request,id):
	feeds=newsfeed.objects.get(id=id)
	form=commentform(request.POST)
	form.instance.post_id=feeds.id
	if request.method=='POST':
		form=commentform(request.POST)
		form.instance.post_id=feeds.id
		if form.is_valid():
			form.save()
			return redirect('/')
	context={'form':form}
	return render(request,'addcomments.html',context)
	
	

