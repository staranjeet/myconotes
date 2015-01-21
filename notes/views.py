from django.shortcuts import render_to_response
import random,string
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from notes.models import *
from django.core.context_processors import csrf
from django.template import RequestContext
import datetime
from django.utils import timezone


# Create your views here.

def index(request,url=None):
	c = {}
	c.update(csrf(request))
	# if url:
	# 	print 'hello'
	# 	existingNotes =  Notes.objects.filter(url=url)
	return render_to_response('index.html',context_instance=RequestContext(request))

def viewnotes(request,url=None):
	c = {}
	c.update(csrf(request))
	if url:
		print 'hello'
		existingNotes =  Notes.objects.filter(url=url)
	return render_to_response('notes.html',{'existingNotes':existingNotes,'theUrl':url},context_instance=RequestContext(request))
def newurl(request):
	newurl = ''.join([random.choice(string.letters + string.digits) for i in range(6)])

	existingUrl=Notes.objects.filter(url=newurl)
	if existingUrl:
		newurl = ''.join([random.choice(string.letters + string.digits) for i in range(6)])
	redirecturl='/notes/'+newurl
	return HttpResponseRedirect(redirecturl)

def savenote(request):
	if request.POST:
		note=request.POST['notes']
		url = request.POST['url']
		if 'title' in request.POST:
			title=request.POST['title']
			title=title.title()
		else:
			title=None
		noteid = ''.join([random.choice(string.letters + string.digits) for i in range(10)])
		print note,url
		newNote=Notes(url=url,note=note,noteGenDate=timezone.now(),noteid=noteid,title=title)
		newNote.save()
		redirecturl='/notes/'+url
		return HttpResponseRedirect(redirecturl)

def deletenote(request,noteid=None):
	print 'kl'
	if request.GET:
		noteid=request.GET['q']
		print noteid
		n = Notes.objects.get(noteid=noteid)
		#print len(n)
		url = n.url
		n.delete()
		redirecturl='/notes/'+url
		return HttpResponseRedirect(redirecturl)



