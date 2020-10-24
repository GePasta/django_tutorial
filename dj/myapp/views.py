from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta

def view_1(request):
    return HttpResponse("view_1 content")


def default(request):
    return HttpResponse("domyslny komunikat")


def about(request):
    return HttpResponse("Adam i Tomek")


def death_time(request):
    result = datetime.now() + timedelta(years=10)
    return HttpResponse(f"Umrzemy - {result}")
