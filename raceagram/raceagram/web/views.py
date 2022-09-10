
from django.shortcuts import render, redirect

from raceagram.web.models import Profile, CarPhoto


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    context = {
        'hide_additional_nav_items': True
    }
    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    car_photos = set(
        CarPhoto.objects. \
        prefetch_related('tagged_cars').filter(tagged_cars__user_profile=profile))
    context = {
        'car_photos': car_photos,
    }
    return render(request, 'dashboard.html', context)


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


def show_car_photo_details(request, pk):
    car_photo = CarPhoto.objects \
        .prefetch_related('tagged_cars') \
        .get(pk=pk)
    context = {
        'car_photo': car_photo
    }
    return render(request, 'photo_details.html', context)


def like_car_photo(request, pk):
    car_photo = CarPhoto.objects.get(pk=pk)
    car_photo.likes += 1
    car_photo.save()
    return redirect('car photo details', pk)


def show_best_cars(request):
    bestt_cars = CarPhoto.objects.all()
    context = {
        'bestt_cars': bestt_cars
    }
    return render(request, 'best_cars.html', context)

