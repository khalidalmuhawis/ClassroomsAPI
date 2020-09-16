from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from datetime import datetime
from classes.models import Classroom, Student
from .serializers import RegisterSerializer, ClassroomSerializer, ClassroomDetailsSerializer,ClassroomCreateSerializer,ClassroomUpdateSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated


class Register(CreateAPIView):
	serializer_class = RegisterSerializer


class ClassroomList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomSerializer


class ClassroomDetail(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class ClassroomCreate(CreateAPIView):
	serializer_class = ClassroomCreateSerializer

	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)



class ClassroomUpdate(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class ClassroomCancel(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'
