from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Fish, Toy
from django.http import HttpResponse
from .forms import FeedingForm

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
    not_fish_toys = Toy.objects.exclude(id__in= fish.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'fish/detail.html', {
        'fish': fish, 
        'feeding_form': feeding_form, 
        'other_toys': not_fish_toys,
        })

class FishCreate(CreateView):
    model = Fish
    fields = ['name', 'date_added', 'description', 'age']

class FishUpdate(UpdateView):
    model = Fish
    fields = ['age', 'description']

class FishDelete(DeleteView):
    model = Fish
    success_url ='/fishes/'

def add_toy(request, fish_id, toy_id):
    Fish.objects.get(id=fish_id).toys.add(toy_id)
    return redirect('detail', fish_id=fish_id)

def add_feeding(request, fish_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit = False)
        new_feeding.fish_id = fish_id
        new_feeding.save()
    return redirect('detail', fish_id=fish_id)

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'description']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'