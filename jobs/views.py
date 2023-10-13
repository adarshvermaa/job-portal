from django.shortcuts import render
from .models import JobCategory,PostJob
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import Http404
from rest_framework import status
from .serializers import PostJobSerializers
from rest_framework import viewsets
from .filters import PostJobFilter
from rest_framework.filters import SearchFilter
import django_filters


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
        

# search jobs

   

class PostJobViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PostJob.objects.all()
    serializer_class = PostJobSerializers
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, SearchFilter]
    filterset_class = PostJobFilter
    search_fields = ['company_name', 'job_title', 'skills', 'description','job_category__category']
    
    #print(str(PostJobFilter(request.GET, queryset=PostJob.objects.all()).query))
    

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        if not queryset.exists():
            return Response({'detail': 'No data found based on the provided filters.'}, status=200)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    




