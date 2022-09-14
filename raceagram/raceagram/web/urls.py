from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from raceagram.web.views.car_photos import show_car_photo_details, edit_car_photo, create_car_photo, like_car_photo, \
    show_best_cars
from raceagram.web.views.cars import create_car, delete_car, edit_car
from raceagram.web.views.generic import show_home, show_dashboard
from raceagram.web.views.profiles import show_profile, edit_profile, create_profile, delete_profile

urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),

    path('profile/', show_profile, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('photo/details/<int:pk>/', show_car_photo_details, name='car photo details'),
    path('photo/add/', create_car_photo, name='create car photo'),
    path('photo/edit/<int:pk>/', edit_car_photo, name='edit car photo'),
    path('photo/like/<int:pk>/', like_car_photo, name='like car photo'),
    path('photo/bestcars/', show_best_cars, name='best cars'),

    path('car/create/', create_car, name='create car'),
    path('car/edit/<int:pk>/', edit_car, name='edit car'),
    path('car/delete/<int:pk>/', delete_car, name='delete car'),
)

if settings.DEBUG:
     urlpatterns += tuple(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
