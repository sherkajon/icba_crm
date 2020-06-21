from django import forms

from .models import Organization


# class AddOrganization(forms.ModelForm):
#
#     class Meta:
#         model = Organization
#         fields = [
#             '__all__'
#         ]


class AddOrganization(forms.Form):
    Name = forms.CharField()
    Category = forms.CharField()
    Address = forms.CharField()
    Website = forms.URLField()
    Email = forms.EmailField()
    Phone = forms.CharField()

