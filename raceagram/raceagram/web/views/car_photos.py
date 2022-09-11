from django.shortcuts import render, redirect

from raceagram.web.models import CarPhoto


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


def create_car_photo(request):
    return render(request, 'photo_create.html')


def edit_car_photo(request):
    return render(request, 'photo_edit.html')
