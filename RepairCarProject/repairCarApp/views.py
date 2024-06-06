from django.shortcuts import render, redirect
from .forms import RepairForm
from repairCarApp.models import Repair

# Create your views here.
def index(request):
    return render(request, 'index.html')
def repairs(request):
    if request.method == "POST":
        form = RepairForm(request.POST, request.FILES)
        if form.is_valid():
            if not request.user.is_anonymous:
                form.instance.user = request.user
                form.save()
                return redirect('repairs')  # Redirect to the same view after adding the flight
    else:
        form = RepairForm()

    repairs = Repair.objects.filter(car__type='Sedan')
    return render(request, "repairs.html", {"repairs": repairs, "form": form})