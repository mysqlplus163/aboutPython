from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from functools import wraps


def check_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        next_url = request.get_full_path()
        if request.session.get("user"):
            return func(request, *args, **kwargs)
        else:
            return redirect("/login/?next={}".format(next_url))
    return inner


def login(request):
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    if user == "alex" and pwd == "alex1234":
        request.session["user"] = user
        rep = redirect("/index/")
        return rep
    return render(request, "login.html")


def logout(request):
    request.session.delete()
    rep = redirect("/login/")
    return rep


@check_login
def index(request):
    current_user = request.session.get("user", None)
    return HttpResponse("Welcome {}!".format(current_user))


from django.views import View
from django.utils.decorators import method_decorator


class Home(View):

    @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super(Home).dispatch(self, request, *args, **kwargs)

    def get(self, request):
        return render(request, "home.html")
