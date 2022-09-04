from django.contrib import admin

from raceagram.web.models import Profile, Car, CarPhoto


class PetInlineAdmin(admin.StackedInline):
    model = Car


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = (PetInlineAdmin,)


@admin.register(Car)
class PetAdmin(admin.ModelAdmin):
    pass


@admin.register(CarPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass