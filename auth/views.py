from rest_framework import generics
from permissions import IsAuthenticatedOrCreate
from django.contrib.auth.models import User
from serializers import SignUpSerializer

class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)
