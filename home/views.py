from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Home
from .serializers import HomeSerializer

class HomeView(APIView):
    def get(self, request):
        home_data = Home.objects.first()  # Assuming there's only one Home instance
        if home_data:
            serializer = HomeSerializer(home_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "No data found"}, status=status.HTTP_404_NOT_FOUND)

# Create your views here.
