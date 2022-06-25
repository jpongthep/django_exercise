from django.shortcuts import render

from .person_data import person_list

def all_data(request):
    context = { "person_list" : person_list}
    return render(request,"PersonData/all_data.html", context)

def django_data(request):
    context = { "person_list" : person_list}
    return render(request,"PersonData/django_data.html", context)

# Create your views here.
