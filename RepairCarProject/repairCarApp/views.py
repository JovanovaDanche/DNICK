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
                return redirect('repairs')
    else:
        form = RepairForm()

    repairs = Repair.objects.filter(car__type='Sedan')
    return render(request, "repairs.html", {"repairs": repairs, "form": form})

def edit_repair(request, id):
    repair_instance = Repair.objects.filter(id=id).get()
    if request.method == "POST":
        repair = RepairForm(request.POST, instance=repair_instance)
        if repair.is_valid():
            repair.save()
        return redirect("repairs")
    else:
        repair = RepairForm(instance=repair_instance)

    return render(request, "edit_repair.html", {"form": repair})