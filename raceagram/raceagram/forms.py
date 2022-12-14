from django import forms

from raceagram.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from raceagram.web.models import Profile, CarPhoto, Car


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter URL',
                }
            ),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter URL',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'min': '1920-01-01'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter email',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter description',
                    'rows': 3
                }
            ),

        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        cars = list(self.instance.car_set.all())
        CarPhoto.objects.filter(tagged_cars__in=cars).delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateCarForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Car
        fields = ('name', 'type', 'made_date')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter car name',

                }
            )
        }


class EditCarForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Car
        exclude = ('user_profile',)


class DeleteCarForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Car
        exclude = ('user_profile',)


class CreateCarPhotoForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    photo = forms.FileField(required=False)

    class Meta:
        model = CarPhoto
        fields = ('photo', 'description', 'tagged_cars')
        widgets = {
            'photo': forms.FileInput(
                attrs={
                    'class': 'form-control-file',

                }
            ),

            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Enter description',

                }
            ),

        }


class EditCarPhotoForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    class Meta:
        model = CarPhoto
        fields = ('photo', 'description', 'tagged_cars')
