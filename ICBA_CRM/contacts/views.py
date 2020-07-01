from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact, Organization
import csv, io
from django.contrib import messages
from .forms import AddOrganization, AddContact


# Create your views here.
# contact.html
def contact(request):
    all_contact_list = all_contacts(request)
    import_csv = excel_import_contacts(request)
    context = {'contacts': all_contact_list, 'messages': import_csv}
    return render(request, 'contact.html', context)


# organization.html
def organization(request):
    all_organization_list = all_organizations(request)
    import_csv = excel_import_organizations(request)
    context = {'organizations': all_organization_list, 'messages': import_csv}
    return render(request, 'organization.html', context)


# mini views

# get all contacts and details
def all_contacts(request):
    contacts = Contact.objects.all()
    return contacts


# get all organizations and details
def all_organizations(request):
    organizations = Organization.objects.all()
    return organizations


# import from csv to contacts table
def excel_import_contacts(request):
    # declaring template
    template = "contact.html"
    data = Contact.objects.all()
    context = {}

    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be First_Name, Last_Name, Email, Phone_Number, designation, Organizations',
        'profiles': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        context = {'messages': "THIS IS NOT A CSV FILE"}
        return render(request, "Message.html", context)

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
            Organizations=Organization.objects.get(Name=column[5])
        )

    return context


# import from csv to organizations table
def excel_import_organizations(request):
    # declaring template
    template = "organization.html"
    data = Organization.objects.all()

    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be Name, Category, Address, Website, Email, Phone',
        'profiles': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        context = {'messages': "THIS IS NOT A CSV FILE"}
        return render(request, "Message.html", context)

    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Organization.objects.update_or_create(
            Name=column[0],
            Category=column[1],
            Address=column[2],
            Website=column[3],
            Email=column[4],
            Phone=column[5]
        )
    context = {}
    return context


def add_New_Organization(request):
    form = AddOrganization()
    if request.method == "POST":
        form = AddOrganization(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/organization')

    context = {
        'form': form
    }
    return render(request, "add_organization.html", context)

    #
    # org_form = AddOrganization(request.GET)
    # if request.method == "POST":
    #     org_form = AddOrganization(request.POST or None)
    #     if org_form.is_valid():
    #         Organization.objects.create(**org_form.cleaned_data)
    #     else:
    #         print(org_form.errors)
    #
    # context = {
    #     'form': org_form
    # }
    # return render(request, "add_organization.html", context)


def add_New_Contact(request):
    form = AddContact()
    if request.method == "POST":
        form = AddContact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact')
    context = {
        'form': form
    }

    return render(request, "add_contact.html", context)


def updateContact(request, pk):
    c = Contact.objects.get(id=pk)
    form = AddContact(instance=c)

    if request.method == "POST":
        form = AddContact(request.POST, instance=c)
        if form.is_valid():
            form.save()
            return redirect('/contact')

    context = {'form': form}
    return render(request, "add_contact.html", context)


def deleteContact(request, pk):
    c = Contact.objects.get(id=pk)
    c.delete()
    return redirect('/contact')


def updateOrganization(request, pk):
    o = Organization.objects.get(id=pk)
    form = AddOrganization(instance=o)

    if request.method == "POST":
        form = AddOrganization(request.POST, instance=o)
        if form.is_valid():
            form.save()
            return redirect('/organization')

    context = {'form': form}
    return render(request, "add_organization.html", context)


def deleteOrganization(request, pk):
    o = Organization.objects.get(id=pk)
    o.delete()
    return redirect('/organization')
