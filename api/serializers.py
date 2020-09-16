from django.contrib.auth.models import User
from rest_framework import serializers
from classes.models import Classroom, Student


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class ClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject', 'name', 'year', 'teacher','id']


class ClassroomDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'


class ClassroomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['subject', 'name', 'year']


class ClassroomUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['subject', 'name', 'year']



