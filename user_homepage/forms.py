from django import forms

class Form(forms.Form):
    city_name = forms.CharField()
    