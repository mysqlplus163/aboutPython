from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from app01.models import Publisher
from app01.serializers import PublisherSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def publisher_list(request):

    if request.method == "GET":
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        return JSONResponse(serializer.data)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PublisherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def publisher_detail(request, pk):
    """
    获取，更新或删除一个 code snippet。
    """
    try:
        publisher = Publisher.objects.get(pk=pk)
    except Publisher.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PublisherSerializer(publisher)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PublisherSerializer(publisher, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        publisher.delete()
        return HttpResponse(status=204)