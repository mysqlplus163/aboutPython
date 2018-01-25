from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from functools import wraps


def check_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        if request.COOKIES.get("user", None):
            return func(request, *args, **kwargs)
        else:
            return redirect("/logout/")
    return inner


def login(request):
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    if user == "alex" and pwd == "alex1234":
        rep = redirect("/index/")
        import datetime
        now = datetime.datetime.now()
        d = datetime.timedelta(seconds=10)
        rep.set_cookie("user", user, expires=now+d)
        return rep
    
    return render(request, "login.html")


def logout(request):
    rep = redirect("/login/")
    rep.delete_cookie("user")
    return rep


@check_login
def index(request):
    current_user = request.COOKIES.get("user", None)
    return HttpResponse("Welcome {}!".format(current_user))


data = []

for i in range(1, 302):
    tmp = {"id": i, "name": "alex-{}".format(i)}
    data.append(tmp)

# def user_list(request):
#
#     # user_list = data[0:10]
#     # user_list = data[10:20]
#     try:
#         current_page = int(request.GET.get("page"))
#     except Exception as e:
#         current_page = 1
#
#     per_page = 10
#
#     # 数据总条数
#     total_count = len(data)
#     # 总页码
#     total_page, more = divmod(total_count, per_page)
#     if more:
#         total_page += 1
#
#     # 页面最多显示多少个页码
#     max_show = 11
#     half_show = int((max_show-1)/2)
#
#     if current_page <= half_show:
#         show_start = 1
#         show_end = max_show
#     else:
#         if current_page + half_show >= total_page:
#             show_start = total_page - max_show
#             show_end = total_page
#         else:
#             show_start = current_page - half_show
#             show_end = current_page + half_show
#
#     # 数据库中获取数据
#     data_start = (current_page - 1) * per_page
#     data_end = current_page * per_page
#
#     user_list = data[data_start:data_end]
#
#     # 生成页面上显示的页码
#     page_html_list = []
#     # 加首页
#     first_li = '<li><a href="/user_list/?page=1">首页</a></li>'
#     page_html_list.append(first_li)
#     # 加上一页
#     if current_page == 1:
#         prev_li = '<li><a href="#">上一页</a></li>'
#     else:
#         prev_li = '<li><a href="/user_list/?page={}">上一页</a></li>'.format(current_page - 1)
#     page_html_list.append(prev_li)
#     for i in range(show_start, show_end+1):
#         if i == current_page:
#             li_tag = '<li class="active"><a href="/user_list/?page={0}">{0}</a></li>'.format(i)
#         else:
#             li_tag = '<li><a href="/user_list/?page={0}">{0}</a></li>'.format(i)
#         page_html_list.append(li_tag)
#
#     # 加下一页
#     if current_page == total_page:
#         next_li = '<li><a href="#">下一页</a></li>'
#     else:
#         next_li = '<li><a href="/user_list/?page={}">下一页</a></li>'.format(current_page+1)
#     page_html_list.append(next_li)
#
#     # 加尾页
#     page_end_li = '<li><a href="/user_list/?page={}">尾页</a></li>'.format(total_page)
#     page_html_list.append(page_end_li)
#
#     page_html = "".join(page_html_list)
#
#     return render(request, "user_list.html", {"user_list": user_list, "page_html": page_html})

from page import Pagination
def user_list(request):
    pager = Pagination(request.GET.get("page"), len(data), request.path_info)
    user_list = data[pager.start:pager.end]
    page_html = pager.page_html()
    return render(request, "user_list.html", {"user_list": user_list, "page_html": page_html})
