from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):

    if request.method == "POST":
        print(request.POST)
        print(request.POST.getlist("author"))
        return HttpResponse("OK")
    return render(request, "index.html")
    pass

