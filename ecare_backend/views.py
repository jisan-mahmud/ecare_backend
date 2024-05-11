from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from django.contrib.auth.models import User

class UserInfo(APIView):
    queryset = User.objects.all()
    serializer_classe = UserSerializer
    def get(self, request):
        serializer = self.serializer_classe(self.queryset.all(), many= True)
        print(self.queryset.all())
        print(self.queryset)
        return Response(serializer.data)
