from django.shortcuts import render
from .models import PostCategory,PostSection
from .serializers import PostCategorySerializers,PostSectionSerializers
from rest_framework.views import APIView
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.

class PostSectionApiview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
            
        try:
            return PostSection.objects.get(pk=pk)
        except PostSection.DoesNotExist:
            raise Http404
    
    def get(self, request, pk=None, format=None):
        current_user = request.user
        if pk:
            data = self.get_object(pk)
            serializer = PostSectionSerializers(data)
            return Response(serializer.data)

        else:
            data = PostSection.objects.filter(user=current_user)
            serializer = PostSectionSerializers(data, many=True)
            if not data.exists():
                return Response({'detail': 'No PostSection found for the current user'}, status=status.HTTP_404_NOT_FOUND)

            return Response(serializer.data)
        # create the employee
    def post(self, request, format=None):
        mutable_data = request.data.copy()
        mutable_data['user'] = request.user.id

        serializer = PostSectionSerializers(data=mutable_data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'PostSection Created Successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
    def patch(self, request, pk=None, format=None):
               
        todo_to_update = PostSection.objects.get(pk=pk)

        serializer = PostSectionSerializers(instance=todo_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'message': 'PostSection Updated Successfully',
           'data': serializer.data
        }

        return response
        # delete the employee
    def delete(self, request, pk, format=None):
        post_to_delete =  PostSection.objects.get(pk=pk)

            # delete the todo
        post_to_delete.delete()

        return Response({
            'message': 'Booking Deleted Successfully'
        })


    
class PostCategoryApiview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
            
        try:
            return PostCategory.objects.get(pk=pk)
        except PostCategory.DoesNotExist:
            raise Http404
    
    def get(self, request, pk=None, format=None):
        current_user = request.user
        if pk:
            data = self.get_object(pk)
            serializer = PostCategorySerializers(data)
            return Response(serializer.data)

        else:
            data = PostCategory.objects.filter(user=current_user)
            serializer = PostCategorySerializers(data, many=True)
            if not data.exists():
                return Response({'detail': 'No PostCategory found for the current user'}, status=status.HTTP_404_NOT_FOUND)

            return Response(serializer.data)
        # create the employee
    def post(self, request, format=None):
        mutable_data = request.data.copy()
        mutable_data['user'] = request.user.id

        serializer = PostCategorySerializers(data=mutable_data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'PostCategory Created Successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
