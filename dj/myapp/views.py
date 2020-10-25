from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render

from .models import Person


def view_1(request):
    return HttpResponse("view_1 content")


def default(request):
    return render(request, "myapp/warning.html")


def about(request):
    persons = Person.objects.order_by("-mass")[:5]

    context = {"persons": persons}
    return render(request, "myapp/about.html", context)


def death_time(request):
    person = Person.objects.get(pk=1)
    result = datetime.now() + timedelta(days=10)
    temp_dict = {"time_of_death": result, "person": person}
    return render(request, "myapp/death.html", temp_dict)
    # return HttpResponse(f"Umrzemy - {result}")
