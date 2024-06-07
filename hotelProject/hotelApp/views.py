from django.shortcuts import render,redirect
from hotelApp.models import Reservation,Room
from hotelApp.forms import ReservationForm,RoomForm
from django.http import Http404, HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    rooms = Room.objects.filter(num_beds__lt=5,is_clean=True)
    return render(request, "index.html", {"rooms": rooms})

def contact_us(request):
    if request.method == "POST":
        reservation = ReservationForm(request.POST, request.FILES)
        if reservation.is_valid():
            if not request.user.is_anonymous:
                reservation.instance.user = request.user
                reservation.save()
                print("Reservation saved successfully!")
                return redirect("index")
        else:
            print(reservation.errors)

    else:
        reservation = ReservationForm()

    return render(request, "contact_us.html", {"form": reservation})
def delete_room(request, id):
    room_instance = Room.objects.filter(id=id).get()
    if request.method == "POST":
        room_instance.delete()
        return redirect("index")

    return render(request, "delete_room.html")
def edit_room(request, id):
    room_instance = Room.objects.filter(id=id).get()
    if request.method == "POST":
        room = RoomForm(request.POST, instance=room_instance)
        if room.is_valid():
            room.save()
        return redirect("index")
    else:
        room = RoomForm(instance=room_instance)

    return render(request, "edit_room.html", {"form": room})

def room_detail(request, room_id):
    try:
        room = Room.objects.get(id=room_id)
    except Room.DoesNotExist:
        raise Http404("Room does not exists!")

    return render(request, "room_details.html", {"room": room})