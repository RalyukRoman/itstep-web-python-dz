from django import forms

class PersonSearchForm(forms.Form):
    full_name = forms.CharField(
        required=False, 
        label="ПІБ людини", 
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Наприклад: Іванов'
        })
    )

    city = forms.CharField(
        required=False, 
        label="Місто", 
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Наприклад: Київ'
        })
    )