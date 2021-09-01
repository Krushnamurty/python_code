from rest_framework import serializers
from .models import *


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Clients
        fields='__all__'


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Projects
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields='__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Projects
        fields=['id','project_name']


class ClientProjectSerializer(serializers.ModelSerializer):
    projects=ProjectSerializer(many=True,read_only=True)

    class Meta:
        model=Clients
        fields=['id','client_name','projects','created_at','created_by']


class ClientsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Clients
        fields='__all__'


class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=['id','name']


class ProjectUserSerializer(serializers.ModelSerializer):
    users=UserIdSerializer(many=True)

    class Meta:
        model=Projects
        fields=['id','project_name','client','users','created_at','created_by']




