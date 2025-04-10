from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from .models import Experience, Education, About  # Removed AboutMe import
from .serializers import AboutSerializer, ExperienceSerializer, EducationSerializer  # Removed AboutMeSerializer
from rest_framework.permissions import AllowAny

class AboutMeView(APIView):
    permission_classes = [AllowAny]  # Allow any user to access this view
    def get(self, request):
        about_instance = About.objects.first()  # Use About model instead of AboutMe
        if about_instance:
            serializer = AboutSerializer(about_instance)  # Use AboutSerializer
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "No data found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        about_instance = About.objects.first()  # Use About model here as well
        if about_instance:
            serializer = AboutSerializer(about_instance, data=request.data, partial=True)
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

class AboutDataView(APIView):
    def get(self, request):
        about_instance = About.objects.first()
        if about_instance:
            serializer = AboutSerializer(about_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "No about data found"}, status=status.HTTP_404_NOT_FOUND)

class AboutUpdateView(APIView):
    permission_classes = [AllowAny] 
    def put(self, request):
        about_instance = About.objects.first()
        if not about_instance:
            return Response({"error": "No about data found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AboutSerializer(about_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

