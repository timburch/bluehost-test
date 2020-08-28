from django import forms
from .models import Product

class AddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['CustomerId', 'ProductName', 'Domain', 'DurationMonths']

class UploadForm(forms.Form):
    file = forms.FileField()