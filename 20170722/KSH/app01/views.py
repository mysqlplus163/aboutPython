from django.shortcuts import render, HttpResponse
from app01 import models
import json

# Create your views here.


def index(request):
    contents = models.Product.objects.all()
    return render(request, "index.html", {"contents": contents})


def add(request):
    msg = {"code": "error"}

    product_info = request.POST
    try:
        new_obj = models.Product.objects.create(**{k: product_info[k] for k in product_info})
        msg["id"] = new_obj.id
        msg["name"] = new_obj.name
        msg["date"] = new_obj.date
        msg["status"] = new_obj.get_status_display()
        msg["code"] = "success"
        print(msg)
        print(new_obj.status)
        print(new_obj.get_status_display())
    except Exception as e:
        msg["info"] = str(e)
    return HttpResponse(json.dumps(msg))


def delete(request):
    product_id = request.POST.get("id")
    msg = {}
    obj = models.Product.objects.filter(id=product_id).first()
    if obj:
        # obj.delete()
        print(obj, "delete...")
        msg["code"] = "success"
        msg["info"] = "<{}> 删除成功".format(obj.name)
        msg["delete_id"] = obj.id
    else:
        msg["code"] = "error"
        msg["info"] = "无效的产品id"

    return HttpResponse(json.dumps(msg))
