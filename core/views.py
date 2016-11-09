from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'index.html')

def contact(request):
	return render(request, 'contact.html')

def user(request):
	return render(request, 'user.html')

def user_list(request):
	return render(request, 'user_list.html')
