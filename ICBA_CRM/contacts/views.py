from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, Organization
import csv, io
from django.contrib import messages


# Create your views here.
def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'contact.html', {'contacts': contacts})


def organization(request):
    organizations = Organization.objects.all()
    return render(request, 'organization.html', {'organizations': organizations})


def excel_import_contacts(request):
    # declaring template
    template = "profile_upload.html"
    data = Contact.objects.all()


    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'profiles': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')

    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Contact.objects.update_or_create(
            First_Name=column[0],
            Last_Name=column[1],
            Email=column[2],
            Phone_Number=column[3],
            designation=column[4],
            Organizations= Organization.objects.get(Name=column[5])
        )
    context = {}
    return render(request, template, context)

