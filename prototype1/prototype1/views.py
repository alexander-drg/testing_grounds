from django.shortcuts import redirect
from .models import Cart, Product
from .forms import ProductForm
from django.shortcuts import render
from .models import Product
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from .forms import ContactForm
from django.http import HttpResponseRedirect


def homepage(request):
    # This view is accessible only to logged-in users
    username = request.user.username
    products = Product.objects.all()
    return render(request, 'homepage.html', {'username': username, 'products': products})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            Contact.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(request.path)
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})


def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            # Assuming you have a CustomUser model with an 'email' field
            User = get_user_model()
            user = User.objects.create_user(
                email=email, username=username, password=password)

            # Additional user data can be saved here if needed

            user.save()

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('/')
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {'form': form})


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse("Success")
        else:
            messages.error(request, 'Invalid username or password')
            return redirect("/")
    else:
        return render(request, 'log-in.html')


def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')
    else:
        return render(request, 'signout.html')


def product(request, pk):
    # Retrieve a single product by its primary key
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product.html", {'product': product})

# views.py


def add_to_cart(request, pk):
    # Retrieve the product object from the database
    product = get_object_or_404(Product, pk=pk)

    # Add the product to the cart
    cart = Cart(request)
    cart.add(product)

    # Redirect the user to the cart page
    # Redirect to the cart page
    return render(request, "cart.html", {'product': product})
