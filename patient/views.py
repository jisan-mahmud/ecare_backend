from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer, PatientRegister
from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework.decorators import api_view

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
        return Response({'email': 'Email succesfully activated.'})
    else:
        return redirect({'error': 'Try again. Email not activate!'})
