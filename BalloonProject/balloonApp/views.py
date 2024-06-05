from django.shortcuts import render, redirect
from balloonApp.models import Flight
from .forms import FlightForm
# Create your views here.
def index(request):
    return render(request, 'index.html')


def flights(request):
    if request.method == "POST":
        form = FlightForm(request.POST, request.FILES)
        if form.is_valid():
            if not request.user.is_anonymous:
                form.instance.user = request.user
                form.save()
                return redirect('flights')  # Redirect to the same view after adding the flight
    else:
        form = FlightForm()

    flights = Flight.objects.filter(airportBegin='Sk')
    return render(request, "flights.html", {"flights": flights, "form": form})

