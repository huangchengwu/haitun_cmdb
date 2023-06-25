from django.shortcuts import render
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
import json
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http.response import HttpResponse


# Create your views here.
class clusterViewSet(ModelViewSet):
    queryset = cluster.objects.all()
    serializer_class = clusterSerializer
    # # 过滤
    filter_fields = ("id", "htmlName")
    # 排序
    ordering_fields = "id"

    # 自定义方法
    @action(methods=["post"], detail=False, url_path="exec_task")
    def exec_task(self, request, *args, **kwargs):
        print(request.method, args, kwargs, request.data)
        dd = {"w": "ww", "ee": "ttt"}

        return Response(dd)


def echo(request):
        print("===",request)
   
        return HttpResponse("11")
