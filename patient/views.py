from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Patient
from .serializers import (
    PatientSerializer,
    PatientRegister,
    UserLoginSerializer
    )
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

# header file for email confirmation
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientRegisterAPIView(APIView):
    serializer_class = PatientRegister
    def post(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Email sent for confirm email address
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id.'
            message = render_to_string('active_email.html',{
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(str(user.pk).encode()),
                'token':default_token_generator.make_token(user),
            }
            )
            to_email = user.email
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()

            return Response(serializer.data)
        return Response({'errors': serializer.errors})

@api_view(['GET'])
def active(request, uid, token):
    id = urlsafe_base64_decode(uid).decode()
    user = User.objects.get(pk= id)
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        token, create = Token.objects.get_or_create(user= user)
        response = {
            'success': True,
            'username': user.username,
            'email': user.email,
            'token': token.key
        }
        return Response(response, status= status.HTTP_200_OK)
    else:
        return Response({'error': 'Try again. Email not activate!'}, status = status.HTTP_404_NOT_FOUND)


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            user = authenticate(username= username, password= password)
            if user and (user.is_active == True):
                token, create = Token.objects.get_or_create(user= user)

                #update last login time
                time = timezone.now()
                user.last_login = time
                user.save(update_fields= ['last_login'])

                response = {
                    'success': True,
                    'id': user.id,
                    'username': user.username,
                    'token': token.key
                }
                return Response(response, status= status.HTTP_200_OK)
            else:
                response = {
                    'success': False,
                    'massage': 'user credentials invalid.'
                }
                return Response(response, status= status.HTTP_401_UNAUTHORIZED)
        return Response({'error': serializer.errors}, status= status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Retrieve the user's token
        user_token = Token.objects.filter(user=request.user)

        # Delete the user's token
        user_token.delete()

        # Create the response
        response_data = {
            'success': True,
            'id': request.user.id,
            'message': 'User successfully logged out.'
        }

        # Return the response
        return Response(response_data, status=status.HTTP_200_OK)
