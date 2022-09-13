from django.shortcuts import render, redirect
from raceagram.forms import CreateCarForm, EditCarForm, DeleteCarForm
from raceagram.web.helpers import get_profile
from raceagram.web.models import Car


def create_car(request):
    instance = Car(user_profile=get_profile())
    if request.method == 'POST':
        form = CreateCarForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CreateCarForm(instance=instance)

    context = {
        'form': form
    }
    return render(request, 'car_create.html', context)


def edit_car(request, pk):
    instance = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditCarForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditCarForm(instance=instance)

    context = {
        'form': form,
        'car': instance
    }
    return render(request, 'car_edit.html', context)


def delete_car(request, pk):
    instance = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteCarForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = DeleteCarForm(instance=instance)

    context = {
        'form': form,
        'car': instance
    }
    return render(request, 'car_delete.html', context)
