from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def fish_index(request):
    fishes = Fish.objects.all()
    return render(request, 'fish/index.html', {'fishes': fishes})

def fish_detail(request, fish_id):
    fish = Fish.objects.get(id=fish_id)
    return render(request, 'fish/detail.html', {'fish': fish})

class FishCreate(CreateView):
    model = Fish
    fields = '__all__'

class FishUpdate(UpdateView):
    model = Fish
    fields = ['age', 'description']
    
class FishDelete(DeleteView):
    model = Fish
    success_url ='/fishes/'