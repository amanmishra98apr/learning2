from django import forms
from testapp.models import FirstTable

class FirstTableForm(forms.ModelForm):
    class Meta:
        model=FirstTable
        fields="__all__"
