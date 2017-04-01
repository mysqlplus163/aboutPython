from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_http_methods
from . import models
import json

# Create your views here.


@require_http_methods(["GET", "POST"])
def author_list(request):
    queryset = models.Author.objects.all()
    ret = []
    for i in queryset:
        tmp = {"id": i.id, "name": i.name}
        ret.append(tmp)
    return HttpResponse(json.dumps(ret))
