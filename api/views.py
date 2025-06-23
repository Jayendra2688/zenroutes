
import requests
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from .serializers import RouteapiSerializer
from django.conf import settings

class ZenApi(APIView):
    
    def get(self,request):
        data = {
            "message": "Your first working DRF GET API 🎉"
        }
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self,request):
        
        serializer = RouteapiSerializer(data = request.data)        
        
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
        
        source = serializer.validated_data['source']
        destination = serializer.validated_data['destination']
        
        url = f"https://maps.googleapis.com/maps/api/directions/json?origin={source}&destination={destination}&key={settings.GOOGLE_MAPS_API_KEY}&alternatives=true"
        
        response = requests.get(url)        
        response = response.json()
        routes = response["routes"]
        print(len(routes))
        
        if response['status']!="OK":
            return Response({"error": "No routes found for the given locations."},status=status.HTTP_400_BAD_REQUEST)
        
        top_3_routes = sorted(routes, key=lambda x: x["legs"][0]["duration"]["value"])[:3]
        
        print([r["legs"][0]["duration"]["text"] for r in top_3_routes])
        
        return Response(top_3_routes,status=status.HTTP_201_CREATED)
    