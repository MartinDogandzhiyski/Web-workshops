from django.shortcuts import render, redirect

from raceagram.forms import CreateCarForm
from raceagram.web.helpers import get_profile
from raceagram.web.models import Car


def create_car(request):
    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CreateCarForm()

    context = {
        'form': form
    }
    return render(request, 'car_create.html', context)


def edit_car(request):
    return render(request, 'car_edit.html')


def delete_car(request):
    return render(request, 'car_delete.html')