from django.shortcuts import render
from api.models import User, Object
from api.serializers import UserSerializer, ObjectSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework.decorators import api_view

# {"count":3,"next":null,"previous":null,"results":[{"id":1,"name":"toto"},{"id":2,"name":"oliv"},{"id":3,"name":"from_api"}]}
#class UserList(generics.ListCreateAPIView):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer

#[{"id": 1, "name": "toto"}, {"id": 2, "name": "oliv"}, {"id": 3, "name": "from_api"}, {"id": 4, "name": "with_serializer"}]
@csrf_exempt
@api_view(['GET', 'POST'])
def UserList(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET', 'POST'])
def ObjectList(request):
    if request.method == 'GET':
        objects = Object.objects.all()
        serializer = ObjectSerializer(objects, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = ObjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ObjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
