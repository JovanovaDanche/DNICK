from balloonApp.models import Flight
from django import forms
class FlightForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FlightForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
    class Meta:
        model = Flight
        fields = "__all__"
        exclude = ["user"]