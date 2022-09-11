from django.shortcuts import render, redirect

from raceagram.web.models import CarPhoto

from raceagram.web.helpers import get_profile


def show_home(request):
    context = {
        'hide_additional_nav_items': True
    }
    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    if not profile:
        redirect('401')
    car_photos = set(
        CarPhoto.objects. \
            prefetch_related('tagged_cars').filter(tagged_cars__user_profile=profile).distinct())
    context = {
        'car_photos': car_photos,
    }
    return render(request, 'dashboard.html', context)