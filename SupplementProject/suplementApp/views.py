from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from suplementApp.models import Supplement
from suplementApp.forms import SupplementForm
# Create your views here.
def index(request):
    supplements = Supplement.objects.all()

    return render(request, "index.html", {"supplements": supplements})
def add_supplement(request):
    if request.method == "POST":
        supplement = SupplementForm(request.POST, request.FILES)
        if supplement.is_valid():
            supplement.save()
            print("Supplement saved successfully!")
            return redirect("index")
            supplement = SupplementForm()
        else:
            print(supplement.errors)

    else:
        supplement = SupplementForm()

    return render(request, "add_supplement.html", {"form": supplement})

def supplement_detail(request, supplement_id):
    try:
        supplement = Supplement.objects.get(id=supplement_id)
    except Supplement.DoesNotExist:
        raise Http404("Supplement does not exists!")

    return render(request, "supplement_details.html", {"supplement": supplement})