from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    city = forms.CharField(required=True)
    phone = forms.IntegerField(required=True)
    image = forms.ImageField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'city', 'phone', 'image', 'password1', 'password2', )