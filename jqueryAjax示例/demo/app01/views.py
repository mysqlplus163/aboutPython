from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    if request.method == "POST":
        print(request.POST.get("data"))
        return HttpResponse("OK")
    else:
        return render(request, "index.html")

