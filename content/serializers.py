from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Content


class UserRegistratoinSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ["username", "password", "email"]

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get("username"),
            password=validated_data.get("password"),
            email=validated_data.get("email"),
        )
        return user


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["id", "topic", "generated_text", "tags", "created_at"]
