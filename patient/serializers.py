from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many= False)

    class Meta:
        model = Patient
        fields = '__all__'


class PatientRegister(serializers.ModelSerializer):
    confirm_password = serializers.CharField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Password does\'t match!'})

        if User.objects.filter(email= email).exists():
            raise serializers.ValidationError({'email': 'This email already exits!'})
        user = User.objects.create_user(
            username= username,
            email= email,
            first_name= first_name,
            last_name= last_name
        )
        user.set_password(password)
        user.is_active = False
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()