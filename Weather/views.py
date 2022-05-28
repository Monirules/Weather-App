from django.shortcuts import render
from multiprocessing import context
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
import urllib.request
import json
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.mail import send_mail
import requests
from .models import City


def home(request):
		if request.method == 'POST':

			city = request.POST['city']

			source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
			city + '&units=metric&appid=f970c0aaadfbb02ba90820d9f4643c8e').read()
			list_of_data = json.loads(source)

			data = {
				"country_code": str(list_of_data['sys']['country']),
				"coordinate": str(list_of_data['coord']['lon']) + ', '
				+ str(list_of_data['coord']['lat']),

				"temp": str(list_of_data['main']['temp']) + ' °C',
				"pressure": str(list_of_data['main']['pressure']),
				"humidity": str(list_of_data['main']['humidity']),
				'main': str(list_of_data['weather'][0]['main']),
				'description': str(list_of_data['weather'][0]['description']),
				'icon': list_of_data['weather'][0]['icon'],
			}
			print(data)
		else:
			data = {}

		return render(request, 'index.html', data)


def home2(request):

	if request.method == 'POST':
		name = request.POST['name']
		citys = City(name=name)
		citys.save()
		
		cities = City.objects.filter(id=request.user.id)
		url = 'http://api.openweathermap.org/data/2.5/weather?q=' + name + '&units=metric&appid=f970c0aaadfbb02ba90820d9f4643c8e'
		weather_data = []

		for city in cities:

				r = requests.get(url.format(city)).json()
				city_weather = {
					'city' : r['sys']['country'],
					'temperature' : r['main']['temp'],
					'description' : r['weather'][0]['description'],
					'icon' : r['weather'][0]['icon'],
				}

				weather_data.append(city_weather)

		context = {'weather_data' : weather_data}
		return render(request, 'home2.html', context)
	
	else:
		return render(request, 'home2.html')


def register(request):

	if request.method == "POST":
		username = request.POST['username']	
		email = request.POST['email']
		password = request.POST['password']

		if User.objects.filter(username = username).exists():
			messages.error(request, "Username already exist")
			return redirect('/register')

		if User.objects.filter(email = email).exists():
			messages.error(request, "Email already exist")
			return redirect('/register')

		if not request.POST.get('email').endswith('@gmail.com'):
			messages.error(request, "We accept Gmail only :)")
			return redirect('/register')

		else:
			user = User.objects.create_user(username = username, password=password, email=email)
			user.save()
			
			reg = request.POST.get('username')
			messages.info(request, 'Account created for - Mr. ' + reg)
			return redirect('/register')
		
		
	else:
		return render (request, 'registration.html')



def loginpage(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)

		if user is not None:	
			auth.login(request, user) 
			return redirect('home2')		
		else:
			messages.error(request, 'Wrong username or password')
			return redirect('loginpage')
		
	else:
		return render(request,'loginpage.html')


def logout(request):
	auth.logout(request)
	return redirect('loginpage')

