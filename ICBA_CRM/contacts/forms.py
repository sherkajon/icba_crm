from django import forms
from .models import Organization, Contact


class AddOrganization(forms.ModelForm):
    class Meta:
        model = Organization
        #fields = ['Name', 'Category', 'Address', 'Website', 'Email', 'Phone']
        fields = '__all__'
        # widgets = '__all__'
        #     'Name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'Category': forms.TextInput(attrs={'class': 'form-control'}),
        #     'Address': forms.TextInput(attrs={'class': 'form-control'}),
        #     'Website': forms.URLInput(attrs={'class': 'form-control'}),
        #     'Email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'Phone': forms.NumberInput(attrs={'class': 'form-control'})
        # }


class AddContact(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['First_Name', 'Last_Name', 'Email', 'Phone_Number', 'designation', 'Organizations']
        # widgets = {
        #     'Name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'Category': forms.TextInput(attrs={'class': 'form-control'}),
        #     'Address': forms.TextInput(attrs={'class': 'form-control'}),
        #     'Website': forms.URLInput(attrs={'class': 'form-control'}),
        #     'Email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'Phone': forms.NumberInput(attrs={'class': 'form-control'})
        # }

# class AddOrganization(forms.Form):
#     Name = forms.CharField()
#     Category = forms.CharField()
#     Address = forms.CharField()
#     Website = forms.URLField()
#     Email = forms.EmailField()
#     Phone = forms.CharField()
