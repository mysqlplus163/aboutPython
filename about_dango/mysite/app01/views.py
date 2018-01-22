from django.shortcuts import render, HttpResponse
from django.urls import reverse
from django.http import Http404, HttpResponseNotFound

# Create your views here.


def url_test(request, *args):
    print(args)
    print(reverse("app:app01_booktest", args=("2018",)))

    # return HttpResponse("OK")
    return render(request, "view02/view02.html")


def view_test(request):
    return HttpResponse("OK")
    raise Http404("找不到啊")