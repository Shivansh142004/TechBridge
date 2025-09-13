from django import forms 
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm): # This form is used to create or update a Tweet
    class Meta: # Meta class to specify model and fields
        model = Tweet # The model associated with this form
        fields = ['text'] # The field to be included in the form 

class UserRegistrationForm(UserCreationForm): # This form is used for user registration
    email = forms.EmailField(required=True) # Email field is requred for registation
    ROLE_CHOICES = [   # Choices for user roles
        ('developer', 'Developer'),
        ('thinker', 'Thinker'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True) #Role field with choices
    class Meta: #Meta class to specify model and fields
        model = User # esh line me  ham user model ko specify kar rahe hai 
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name') # Field to be include in the form
