from django import forms

class DataInputForm(forms.Form):
    data = forms.CharField(widget=forms.Textarea, required=False)
    csv_file = forms.FileField(required=False)
