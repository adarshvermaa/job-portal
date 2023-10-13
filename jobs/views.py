from django.shortcuts import render
from .models import JobCategory,PostJob
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import Http404
from rest_framework import status
from .serializers import PostJobSerializers


class PostJobApiview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return PostJob.objects.get(pk=pk)
        except PostJob.DoesNotExist:
            raise Http404
        # get the employee by id otherwise all the employee
    def get(self, request, pk=None, format=None):
        if pk:
            postjob= self.get_object(pk)
            serializer = PostJobSerializers(postjob,context={'request': request})
            return Response(serializer.data)

        else:
            data = PostJob.objects.filter()
            serializer = PostJobSerializers(data, many=True,context={'request': request})
            return Response(serializer.data)
        

