from rest_framework import serializers

class RouteapiSerializer(serializers.Serializer):
    source = serializers.CharField()
    destination = serializers.CharField()