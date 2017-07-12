from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist

from array import array

#Model
from .models import EventDetails, User, Event, Response

#Python Lib
import json
import hashlib
import uuid

# Create your views here.
def index(request):
	#return HttpResponse("Hello")
	if 'login' in request.session and request.session['login']:
		user = User.objects.get(id=request.session['userid'])

		opt = 0

		try:
			import sys
			query = []
			event = Event.objects.filter(userID=user)
			length = len(event)
			print('[DEBUG INDEX] Object Event Length = ' + str(length))
			if length == 0:
				raise ObjectDoesNotExist('No event!')
			for item in event:
				print('[DEBUG INDEX] Get Event ID = ' + str(item.id))

				details = EventDetails.objects.filter(eventID=item)
				query.extend(details)
			
			return render(request, 'form/show.html',{'query':query, 'ctr':1})
		except ObjectDoesNotExist:
			print('Event blm ada')
			return redirect('addEvent')
	return redirect('login')

def login(request):
	#return HttpResponse("Hello")
	if request.method == "POST":
		req = request.POST

		email = req['email']
		pwd = req['pwd']

		try:
			user = User.objects.get(email=email)
			hash_pwd = user.passHash

			if cek_pwd(pwd, hash_pwd):
				print('id ketemu')

				request.session['login'] = True
				request.session['userid'] = user.id
				request.session['email'] = user.email
				request.session['name'] = user.Fname + ' ' + user.Lname
				#request.session['objek'] = user

				print('[DEBUG LOGIN] userID : ' + str(user.id))
				print('[DEBUG LOGIN] Email : ' + user.email)
				print('[DEBUG LOGIN] Name : ' + user.Fname + ' ' + user.Lname)

				#objevent, created = Event.objects.get_or_create(userID=User.objects.get(userID=request.session['userid']))
				 

				return redirect('index')

		except ObjectDoesNotExist:
			print('ga ada!')

	elif 'login' in request.session and request.session['login']:
		return redirect('index')


	return render(request, 'form/login.html',{})

def register(request):
	if(request.method == "POST"):
		req = request.POST

		fname = req['Fname']
		lname = req['Lname']
		email = req['email']
		pwd = req['pwd']

		User.objects.create(Fname=fname, Lname=lname, email=email, passHash=hash_pass(pwd))
		print('[DEBUG REGISTER] SUCCESS')

		return redirect('login')
	return render(request, 'form/register.html',{})


def logout(request):
	request.session.flush()
	return redirect('login')

def add(request):
	if request.method == "POST":

		req = request.POST
		jsondata = json.loads(str(req['jsondata']))
		jsondata = json.dumps(jsondata)


		event = Event.objects.get(id=req['event'])

		EventDetails.objects.create(name=req['name'],jsondata=str(jsondata),eventID=event)
		return redirect('index')

	elif 'login' in request.session and request.session['login']:
		#query = EventDetails.objects.all()
		query = Event.objects.filter(userID=request.session['userid'])
		return render(request, 'form/addForm.html',{'query':query})

def addEvent(request):
	if request.method == "POST":

		req = request.POST
		eventName = req['name'];

		user = User.objects.get(id=request.session['userid'])

		Event.objects.create(name=eventName,userID=user)
		return redirect('index')
	elif 'login' in request.session and request.session['login']:
		#query = EventDetails.objects.all()
		return render(request, 'form/addEvent.html',{})

def editForm(request):
	if request.method == "POST":
		req = request.POST

		id_form = int(req['id_form'])
		print('[DEBUG UPDATE] id_form = ' + req['id_form'])


		edit = EventDetails.objects.get(id=id_form)
		edit.jsondata = req['jsondata']
		edit.name = req['name']
		edit.save()
		print('[DEBUG UPDATE] UPDATE SUCCESS')

	return redirect('index')


def renderForm(request):
	if request.method == "POST":
		req = request.POST
		id_item = int(request.POST['id_item'])
		query = EventDetails.objects.get(id=id_item)

		id_event = int(req['id_event'])
		#event = Event.objects.get(id=id_event)

		if request.POST['submit'] == 'delete':
			print("[DEBUG DELETE] DELETE FORM ID " + str(id_item));
			query.delete();
			return redirect('index')

		elif req['submit'] == 'edit':
			eventdetail = EventDetails.objects.get(id=id_item)
			return render(request, 'form/editForm.html',{'detail':eventdetail})

		else :
			#query = query[0]
			return render(request, 'form/testrender.html', {'query':query, 'id_form':id_item, 'id_event':id_event})
	return redirect('index')

def hash_pass(pwd):
	salt = uuid.uuid4().hex
	return hashlib.sha256(pwd.encode() + salt.encode()).hexdigest() + ':' + salt

def cek_pwd(pwd, hash_pwd):
	password, salt = hash_pwd.split(':')
	return password == hashlib.sha256(pwd.encode() + salt.encode()).hexdigest()

def responseForm(request):
	if request.method == "POST":
		req = request.POST
		jsondata = json.loads(str(req['hiddenIn']))
		jsondata = json.dumps(jsondata)


		event = Event.objects.get(eventID=req['eventid'])

		ResponseDetails.objects.create(responseJSON=str(jsondata),imagePath='a',idCardPath='a',eventID=event)