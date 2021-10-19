from django.shortcuts import render
from .models import Fish
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Hi testing :)</h1>')

def about(request):
    return render(request, 'about.html')

def fish_index(request):
    fishes = Fish.objects.all()
    return render(request, 'fish/index.html', {'fishes': fishes})

def fish_detail(request, fish_id):
    fish = Fish.objects.get(id=fish_id)
    return render(request, 'fish/detail.html', {'fish': fish})