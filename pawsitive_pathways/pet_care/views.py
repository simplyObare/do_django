from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Service
from .forms import PetServiceSelectionForm


@login_required
def service_list(request):
    services = Service.objects.all()
    return render(request, "petcare/service_list.html", {"services": services})


@login_required
def select_service(request):
    if request.method == "POST":
        form = PetServiceSelectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("service_list")
    else:
        form = PetServiceSelectionForm()
    return render(request, "petcare/select_service.html", {"form": form})
