from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import AppliedJobs
from .serializers import AppliedJobsSerializers
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework import status

class ApplyJobApiview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        user = request.user  # Get the current user

        if pk:
            # If a specific job ID is provided, get that job for the current user
            try:
                apply_job = AppliedJobs.objects.get(pk=pk, resume__user=user)
                serializer = AppliedJobsSerializers(apply_job)
                return Response(serializer.data)
            except AppliedJobs.DoesNotExist:
                return Response({'detail': 'Applied job not found'}, status=status.HTTP_404_NOT_FOUND)

        else:
            # Get all applied jobs for the current user
            data = AppliedJobs.objects.filter(resume__user=user)
            serializer = AppliedJobsSerializers(data, many=True)
            return Response(serializer.data)
        
    def post(self, request, format=None):
            data = request.data
            serializer = AppliedJobsSerializers(data=data)

            serializer.is_valid(raise_exception=True)

            serializer.save()

            # Return Response to User

            response = Response()

            response.data = {
                'message': 'Job appy  Successfully',
                'data': serializer.data
            }

            return response
