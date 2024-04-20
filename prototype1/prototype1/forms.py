from .models import Product
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # Assuming username is a CharField
    username = forms.CharField(max_length=150)

    class Meta:
        model = get_user_model()  # Get the user model dynamically
        fields = ['username', 'email', 'password1',
                  'password2']  # Add other fields here


class ContactForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500',
                'placeholder': 'name@flowbite.com'
            }
        )
    )
    subject = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'block p-3 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 shadow-sm focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 dark:shadow-sm-light',
                'placeholder': 'Let us know how we can help you'
            }
        )
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg shadow-sm border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500',
                'placeholder': 'Leave a comment...',
                'rows': 6
            }
        )
    )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'description']
