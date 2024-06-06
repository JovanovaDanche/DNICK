from django import forms
from repairCarApp.models import Repair

class RepairForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RepairForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Repair
        fields = "__all__"
        exclude = ["user"]