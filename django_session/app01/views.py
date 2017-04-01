from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def login(request):
    print("login...")
    if request.method == "POST":
        print(request.POST)
        request.session["user"] = request.POST.get("username")
        return redirect("/index/")
    else:
        return render(request, "login.html")


def index(request):
    if request.session.get("user", None):
        return render(request, "index.html")
    else:
        return HttpResponse("gun")
