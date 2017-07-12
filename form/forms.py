from django import forms

class JSONForm(forms.ModelForm):
	jsondata = forms.CharField(max_length=255)
	name = forms.CharField(max_length=255)
