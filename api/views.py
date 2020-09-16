from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from datetime import datetime
from clesses.models import Classroom, Student
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated


class Register(CreateAPIView):
	serializer_class = RegisterSerializer
