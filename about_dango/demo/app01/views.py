from django.shortcuts import render, HttpResponse

from django.views import View
from app01 import models
# Create your views here.


def index(request):

    if request.method == "POST":
        print(request.POST)
        print(request.POST.getlist("author"))
        return HttpResponse("OK")
    return render(request, "index.html")
    pass


def upload(request):
    if request.method == "POST":
        obj = request.FILES


# class BooksListView(View):
#     def get(self, request):
#
#         books = models.Book.objects.all()
#         data = []
#         for book in books:
#             book_info = {}
#             book_info["title"] = book.title
#             book_info["publisher"] = book.publisher.name
#             data.append(book_info)
#
#         import json
#         return HttpResponse(json.dumps(data), content_type="application/json")

# class BooksListView(View):
#     def get(self, request):
#         books = models.Book.objects.all()
#         data = []
#         for book in books:
#             from django.forms.models import model_to_dict
#             book_info = model_to_dict(book)
#             data.append(book_info)
#         import json
#         return HttpResponse(json.dumps(data), content_type="application/json")


class BooksListView(View):
    def get(self, request):
        books = models.Book.objects.all()
        from django.core import serializers
        data = serializers.serialize("json", books)
        # return HttpResponse(data, content_type="application/json")
        from django.http import JsonResponse
        import json
        return JsonResponse(json.loads(data), safe=False)


def my_test_view(request):
    data = models.MyTest.objects.all()
    return render(request, "mytest.html", {"data": data})
