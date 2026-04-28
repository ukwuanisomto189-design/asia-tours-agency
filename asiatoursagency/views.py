from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tour
from .forms import TourForm

@login_required
def index(request):
    tours = Tour.objects.filter(created_by=request.user)
    return render(request, 'asiatoursagency/index.html', {'tours': tours})

@login_required
def add_tour(request):
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            tour = form.save(commit=False)
            tour.created_by = request.user
            tour.save()
            return redirect('index')
    else:
        form = TourForm()
    return render(request, 'asiatoursagency/add_tour.html', {'form': form})

@login_required
def edit_tour(request, tour_id):
    tour = Tour.objects.get(id=tour_id)
    if request.method == 'POST':
        form = TourForm(request.POST, instance=tour)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TourForm(instance=tour)
    return render(request, 'asiatoursagency/edit_tour.html', {'form': form, 'tour': tour})

@login_required
def delete_tour(request, tour_id):
    tour = Tour.objects.get(id=tour_id)
    tour.delete()
    return redirect('index')