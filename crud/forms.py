from django import forms
from django.forms.widgets import CheckboxInput
from .models import Vehicle

class VehicleCreateForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ["name", "location", "speed", "avg_speed", "temperature",
                  "fuel_level", "engine_status", "camera1", "camera2", "active"]

    def __init__(self, *args, **kwargs):
        super(VehicleCreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if not visible.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__:
                visible.field.widget.attrs['class'] = 'form-control'
            print(visible)

class VehicleUpdateForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ["name", "location", "speed", "avg_speed", "temperature",
                  "fuel_level", "engine_status", "camera1", "camera2", "active"]

    def __init__(self, *args, **kwargs):
        super(VehicleUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            # print(visible)
            if not visible.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__:
                visible.field.widget.attrs['class'] = 'form-control'
