from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from .models import AboutMe, Experience, Education
from .serializers import AboutMeSerializer, ExperienceSerializer, EducationSerializer

class AboutMeView(APIView):
    def get(self, request):
        about_me = AboutMe.objects.first()  # Assuming there's only one AboutMe instance
        if about_me:
            serializer = AboutMeSerializer(about_me)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "No data found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        about_me = AboutMe.objects.first()
        if about_me:
            serializer = AboutMeSerializer(about_me, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "No data found"}, status=status.HTTP_404_NOT_FOUND)

class ExperienceListCreateView(ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class EducationListCreateView(ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

