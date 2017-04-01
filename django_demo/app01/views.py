from django.shortcuts import render, HttpResponse
import json
from app01 import models
from django.core import serializers


# Create your views here.

data = [1, 2, 3, 4]

data2 = {"a": 1, "b": 2}


def view(request):
    return render(request, "view1.html", {"data": data2})

obj = models.Book.objects.filter(id=1)
print(obj)


def home(request):
    return render(request, "home.html", {"data": data})


def authors(request):
    data = serializers.serialize(
        "json",
        models.Author.objects.all(),
        use_natural_foreign_keys=True
    )
    return HttpResponse(data)


def publishers(request):
    params = request.GET()
    print(params)
    return HttpResponse("OK")

