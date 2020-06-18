from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, Organization, Menu


# Create your views here.
def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'contact.html', {'contacts': contacts})


def organization(request):
    organizations = Organization.objects.all()
    return render(request, 'organization.html', {'organizations': organizations})


def menu(request):
    menus = Menu.objects.all()
    return render(request, 'nav.html', {'menu': menus})

