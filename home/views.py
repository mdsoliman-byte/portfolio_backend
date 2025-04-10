from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Home
from .serializers import HomeSerializer

class HomeView(APIView):
    permission_classes = [AllowAny]  # Anyone can fetch hero data
    def get(self, request):
        home_data = Home.objects.first()  # Assuming there's only one Home instance
        if home_data:
            serializer = HomeSerializer(home_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "No data found"}, status=status.HTTP_404_NOT_FOUND)
class HomeUpdateView(APIView):
    permission_classes = [IsAuthenticated]  # Only logged-in users can update

    def put(self, request):
        print("PUT data:", request.data) 
        home_data = Home.objects.first()
        if home_data:
            serializer = HomeSerializer(home_data, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "No data to update"}, status=status.HTTP_404_NOT_FOUND)
# Create your views here.
