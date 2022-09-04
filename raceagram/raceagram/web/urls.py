from django.urls import path

from raceagram.web.views import show_home, show_dashboard, show_profile, like_car_photo, show_car_photo_details, \
    show_best_cars
urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('profile/', show_profile, name='profile'),
    path('photo/details/<int:pk>/', show_car_photo_details, name='car photo details'),
    path('photo/like/<int:pk>/', like_car_photo, name='like car photo'),
    path('photo/bestcars/', show_best_cars, name='best cars'),
)