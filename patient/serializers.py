from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = '__all__'


class PatientRegister(serializers.ModelSerializer):
    confirm_password = serializers.CharField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'username' : {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'password': {'required': True},
            'confirm_password': {'required': True},
        }


    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password': 'Password does\'t match!'})

        if len(attrs['password']) < 6:
            raise serializers.ValidationError({'password': 'Password is too short!'})

        if User.objects.filter(email= attrs['email']).exists():
            raise serializers.ValidationError({'email': 'This email already exits!'})
        return attrs

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']

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