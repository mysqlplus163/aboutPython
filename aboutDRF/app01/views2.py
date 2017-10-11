from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from app01.models import Publisher
from app01.serializers import PublisherSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def publisher_list(request, format=None):
    """
    列出所有的出版社，或者创建一个新的出版社。
    """
    if request.method == 'GET':
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def publisher_detail(request, pk, format=None):
    """
    获取，更新或删除一个snippet实例。
    """
    try:
        publisher = Publisher.objects.get(pk=pk)
    except Publisher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PublisherSerializer(publisher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)