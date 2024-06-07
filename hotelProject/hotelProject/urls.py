"""
URL configuration for hotelProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hotelApp.views import index,contact_us,delete_room,edit_room, room_detail
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="index"),
    path('contact_us/', contact_us, name="contact_us"),
    path('room/delete/<id>/', delete_room, name="delete room"),
    path('room/edit/<id>/', edit_room, name="edit room"),
    path('room_details/<int:room_id>', room_detail, name="Room details"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
