from .models import Resume,ProfileCompletionStar
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import Http404
from rest_framework import status
from .serializers import ResumeSerializers,ProfileCompletionStarSerializers
from quill.delta import Delta
from django.http import JsonResponse


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
        try:
            current_user = request.user
            mutable_data = request.data.copy()
            mutable_data['user'] = current_user.id

            # Assuming the Quill content is in a field called 'content'
            quill_content_delta = mutable_data.get('content', '')

            # Parse Quill delta
            delta = Delta(quill_content_delta)

            # You can now access and process the contents of the delta
            # For example, to get the HTML, you can use delta.to_html()

            # Save to the database using your serializer
            serializer = ResumeSerializers(data=mutable_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            response = JsonResponse({
                'message': 'Resume Created Successfully',
                'data': serializer.data
            })

            return response

        except Exception as e:
            # Handle exceptions
            return JsonResponse({'error': str(e)}, status=500)
    

    def patch(self, request, pk=None, format=None):
                
            resume_to_update = Resume.objects.get(pk=pk)

            serializer = ResumeSerializers(instance=resume_to_update,data=request.data, partial=True)

            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = Response()

            response.data = {
                'message': 'Resume Updated Successfully',
                'data': serializer.data
            }

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