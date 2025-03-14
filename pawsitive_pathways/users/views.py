from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Pet
from .forms import UserRegistrationForm, UserLoginForm, PetForm


def home(request):
    if request.user.is_authenticated:
        return redirect("pet_list")
    return render(request, "users/home.html")


# User registration
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", {"form": form})


# User login
def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, "users/login.html", {"form": form})


# User logout
def user_logout(request):
    logout(request)
    return redirect("login")


# List all pets for the logged-in user
@login_required
def pet_list(request):
    pets = Pet.objects.filter(user=request.user)
    return render(request, "users/pet_list.html", {"pets": pets})


# Create a new pet
@login_required
def pet_create(request):
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect("pet_list")
    else:
        form = PetForm()
    return render(request, "users/pet_form.html", {"form": form})


# Update an existing pet
@login_required
def pet_update(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, user=request.user)
    if request.method == "POST":
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect("pet_list")
    else:
        form = PetForm(instance=pet)
    return render(request, "users/pet_form.html", {"form": form})


# Delete a pet
@login_required
def pet_delete(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, user=request.user)
    if request.method == "POST":
        pet.delete()
        return redirect("pet_list")
    return render(request, "users/pet_confirm_delete.html", {"pet": pet})
