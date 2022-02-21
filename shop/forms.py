from .models import Category2
from django import forms 


class Category2Form(forms.ModelForm):
    class Meta:
        model = Category2
        fields = '__all__'
    