from django.shortcuts import render
from django.urls import reverse

# Create your views here.


def url_test(request, *args):
    print(args)
    print(reverse("app:app01_booktest", args=("2018",)))

    # return HttpResponse("OK")
    return render(request, "view02/view02.html")