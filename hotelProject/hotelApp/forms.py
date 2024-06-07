from hotelApp.models import Reservation,Room
from django import forms
class ReservationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            # додавање бутстрап во форма
            field.field.widget.attrs["class"] = "form-control"
            # додавање чекбокс бутстрап во форма
            if field.name == 'confirmed':
                field.field.widget.attrs["class"] = "form-check-input"
    class Meta:
        model = Reservation
        exclude = ['user',]
        fields = '__all__'

class RoomForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            # додавање бутстрап во форма
            field.field.widget.attrs["class"] = "form-control"
            # додавање чекбокс бутстрап во форма
            if field.name in ['is_clean', 'balcony']:
                field.field.widget.attrs["class"] = "form-check-input"
    class Meta:
        model = Room
        fields = '__all__'