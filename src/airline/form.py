from django import forms
from airline import models


class AirCraftForm(forms.Form):
    key = []
    value = []
    objects_list = models.Model.objects.all()
    for object in objects_list.all():
        key.append(object.mod_code)
        value.append(object.mod_name)

    alist = zip(key,value)
    model = forms.ChoiceField(choices=alist, label='Select Model', initial='', required=True,)


