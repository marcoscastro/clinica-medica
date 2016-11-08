from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	lista_clientes = ['marcos', 'lucas', 'felipe']
	context = {
		'title': 'bem-vindo(a) a clínica!',
		'clientes': lista_clientes
	}
	return render(request, 'index.html', context)