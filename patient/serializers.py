from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class PatientSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source= 'user.first_name')
    last_name = serializers.CharField(source= 'user.last_name')
    email = serializers.EmailField(source= 'user.email')

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'image', 'email', 'mobile_no']

    def save(self, user):
        first_name = self.validated_data['user'].get('first_name')
        last_name = self.validated_data['user'].get('last_name')
        email = self.validated_data['user'].get('email')
        image = self.validated_data.get('image')
        mobile_no = self.validated_data.get('mobile_no')

        # find object
        user_obj = user
        patient = Patient.objects.get(user= user)

        #update user info
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.email = email
        user.save()

        # update patient info
        patient.image = image
        patient.mobile_no = mobile_no
        patient.save()

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