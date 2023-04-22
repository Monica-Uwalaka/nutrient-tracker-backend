from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Goal

# think about serializer like django forms
class UserSerializer(serializers.Serializer):
    """Serializer for converting Users to and from JSON"""
    username = serializers.CharField(required=True)
    email = serializers.EmailField(max_length=150, required=True)
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)

    def create(self, validated_data):
        """Create A New User"""
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)
    
class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ["id", "user", "calories", "protein", "carbohydrate", "fats", "start_date", "end_date"]
    """Serializer for converting Goals to and from JSON"""
    # calories = serializers.IntegerField(required=True)
    # protein = serializers.IntegerField(required=True)
    # carbohydrate = serializers.IntegerField(required=True)
    # fats = serializers.IntegerField(required=True)
    # start_date = serializers.DateTimeField(required=True)
    # end_date = serializers.DateTimeField(required=True)



    