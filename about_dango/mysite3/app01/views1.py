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
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        if user == "alex" and pwd == "alex1234":
            # 设置session
            request.session["user"] = user
            # 获取跳到登陆页面之前的URL
            next_url = request.GET.get("next")
            # 如果有，就跳转回登陆之前的URL
            if next_url:
                return redirect(next_url)
            # 否则默认跳转到index页面
            else:
                return redirect("/index/")
    return render(request, "login.html")


@check_login
def logout(request):
    # 删除所有当前请求相关的session
    request.session.delete()
    return redirect("/login/")


@check_login
def index(request):
    current_user = request.session.get("user", None)
    return render(request, "index.html", {"user": current_user})


from django.views import View
from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt, csrf_protect


class HomeView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(request, *args, **kwargs)

    # @check_login
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        print("Home View POST method...")
        return redirect("/index/")


class LoginView(View):

    def get(self, request):
        """
        处理GET请求
        """
        return render(request, 'login.html')

    def post(self, request):
        """
        处理POST请求
        """
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'alex' and pwd == "alex1234":
            next_url = request.GET.get("next")
            # 生成随机字符串
            # 写浏览器cookie -> session_id: 随机字符串
            # 写到服务端session：
            # {
            #     "随机字符串": {'user':'alex'}
            # }
            request.session['user'] = user
            request.session.set_expiry(6)
            if next_url:
                return redirect(next_url)
            else:
                return redirect('/index/')
        return render(request, 'login.html')
