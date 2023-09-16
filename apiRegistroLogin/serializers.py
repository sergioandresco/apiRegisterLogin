from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    