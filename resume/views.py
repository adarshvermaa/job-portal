from .models import Resume,ProfileCompletionStar
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import Http404
from rest_framework import status
from .serializers import ResumeSerializers,ProfileCompletionStarSerializers


class ResumeApiview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Resume.objects.get(pk=pk)
        except Resume.DoesNotExist:
            raise Http404
        # get the resume by id otherwise all the resume
    def get(self, request, pk=None, format=None):
        if pk:
            resume= self.get_object(pk)
            serializer = ResumeSerializers(resume,context={'request': request})
            return Response(serializer.data)

        else:
            current_user = request.user
            data = Resume.objects.filter(user=current_user)
            serializer = ResumeSerializers(data, many=True,context={'request': request})
            return Response(serializer.data)
        
    # Post request

    def post(self, request, format=None):
            current_user = request.user
            existing_resume = Resume.objects.filter(user=current_user).first()

            if existing_resume:
                # If a resume already exists, return a response to update the resume
                return Response(
                    {'message': 'Your resume already exists. Please update your resume.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            mutable_data = request.data.copy()
            mutable_data['user'] = current_user.id  
            serializer = ResumeSerializers(data=mutable_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = Response()

            response.data = {
                'message': 'Resume Created Successfully',
                'data': serializer.data
            }

            return response
    

    def patch(self, request, pk=None, format=None):
        current_user = request.user

        # Retrieve the resume to update
        resume_to_update = Resume.objects.get(user=current_user)

        # Check if the user attempting to update the resume is the owner
        if resume_to_update.user != current_user:
            return Response(
                {'message': 'You do not have permission to update this resume.'},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = ResumeSerializers(instance=resume_to_update, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response({
            'message': 'Resume Updated Successfully',
            'data': serializer.data
        })

        return response



class ProfileCompletionStarApiview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return ProfileCompletionStar.objects.get(pk=pk)
        except ProfileCompletionStar.DoesNotExist:
            raise Http404
        # get the ProfileCompletionStar by id otherwise all the ProfileCompletionStar
    def get(self, request, pk=None, format=None):
        if pk:
            ProfileCompletion= self.get_object(pk)
            serializer = ProfileCompletionStarSerializers(ProfileCompletion)
            return Response(serializer.data)

        else:
            current_user = request.user
            data = ProfileCompletionStar.objects.filter(user=current_user)
            serializer = ProfileCompletionStarSerializers(data, many=True)
            return Response(serializer.data)