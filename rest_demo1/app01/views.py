from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


class TestView(APIView):

    def get(self, request, format=None):
        data = {"action": "get"}
        return Response(data)

    def post(self, request, format=None):
        print(request.data)
        data = {"action": "post"}
        return Response({"post_form": data})


@api_view()
def BookList(request):
    data = {"name": "BookList"}
    return Response(data)


def logout(request):
    return render(request, "logout.html")
