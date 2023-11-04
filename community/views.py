from django.shortcuts import render
from .models import CommunityReviews,CommunityParticipation
from .serializers import CommunityParticipationserializers,CommunityReviewsserializers
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class CommunityParticipationApiview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
            
        try:
            return CommunityParticipation.objects.get(pk=pk)
        except CommunityParticipation.DoesNotExist:
            raise Http404
    
    def get(self, request, pk=None, format=None):
        # current_user = request.user
        if pk:
            data = self.get_object(pk)
            serializer = CommunityParticipationserializers(data)
            return Response(serializer.data)

        else:
            data = CommunityParticipation.objects.all()
            serializer = CommunityParticipationserializers(data, many=True)
            if not data.exists():
                return Response({'detail': 'No CommunityParticipation found for the current user'}, status=status.HTTP_404_NOT_FOUND)

            return Response(serializer.data)
        # create the employee
    def post(self, request, format=None):
        mutable_data = request.data.copy()
        mutable_data['user'] = request.user.id

        serializer = CommunityParticipationserializers(data=mutable_data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'CommunityParticipation Created Successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
    def patch(self, request, pk=None, format=None):
               
        todo_to_update = CommunityParticipation.objects.get(pk=pk)

        serializer = CommunityParticipationserializers(instance=todo_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'message': 'CommunityParticipation Updated Successfully',
           'data': serializer.data
        }

        return response
        # delete the employee
    def delete(self, request, pk, format=None):
        post_to_delete =  CommunityParticipation.objects.get(pk=pk)

            # delete the todo
        post_to_delete.delete()

        return Response({
            'message': 'Booking Deleted Successfully'
        })



class CommunityReviewsApiview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
            
        try:
            return CommunityReviews.objects.get(pk=pk)
        except CommunityReviews.DoesNotExist:
            raise Http404
    
    def get(self, request, pk=None, format=None):
        # current_user = request.user
        if pk:
            data = self.get_object(pk)
            serializer = CommunityReviewsserializers(data)
            return Response(serializer.data)

        else:
            data = CommunityReviews.objects.all()
            serializer = CommunityReviewsserializers(data, many=True)
            if not data.exists():
                return Response({'detail': 'No CommunityReviews found for the current user'}, status=status.HTTP_404_NOT_FOUND)

            return Response(serializer.data)
        # create the employee
    def post(self, request, format=None):
        mutable_data = request.data.copy()
        mutable_data['user'] = request.user.id

        serializer = CommunityReviewsserializers(data=mutable_data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'CommunityReviews Created Successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)