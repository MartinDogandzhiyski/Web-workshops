from django.shortcuts import render, redirect

from raceagram.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from raceagram.web.helpers import get_profile
from raceagram.web.models import CarPhoto, Profile


def show_profile(request):
    profile = get_profile()
    total_likes = sum(cp.likes for cp in CarPhoto.objects.filter(tagged_cars__user_profile=profile).distinct())
    total_images = len(CarPhoto.objects.filter(tagged_cars__user_profile=profile).distinct())
    context = {
        'profile': get_profile(),
        'total_likes': total_likes,
        'total_images': total_images,
    }
    return render(request, 'profile_details.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form
    }
    return render(request, 'profile_create.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'profile_edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'profile_delete.html', context)
