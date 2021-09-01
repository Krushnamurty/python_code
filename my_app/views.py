from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.


@method_decorator(csrf_exempt,name='dispatch')
class Client(APIView):
    def get(self,request,pk=None,*args,**kwargs):
        if pk is not None:
            try:
                data=Clients.objects.get(id=pk)
            except:
                return Response({'client':'Not found'})
            serializer=ClientProjectSerializer(data)
            return Response(serializer.data)
        else:
            data=Clients.objects.all()
            serializer=ClientsSerializer(data,many=True)
            return Response(serializer.data)

    def post(self,request,pk=None,*args,**kwargs):
        if pk is not None:
            try:
                client=Clients.objects.get(id=pk).id
            except:
                return Response({'client': 'Not found'})
            project_name=request.data.get("project_name")
            users = request.data.get("users")
            data={"project_name":project_name,"client":client,"users":users}
            serializer=ProjectsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                project_id=Projects.objects.get(project_name=project_name)
                for user in users:
                    data={"id":user.get('id'),"name":user.get('name'),"project":project_id.id}
                    serializer=UserSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors)
                serializer=ProjectUserSerializer(project_id)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            serializer=ClientsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)

    def put(self,request,pk=None,*args,**kwargs):
        if pk is not None:
            try:
                data=Clients.objects.get(id=pk)
            except:
                return Response({'client': 'Not found'})
            serializer=ClientsSerializer(data,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)

    def patch(self,request,pk=None,*args,**kwargs):
        if pk is not None:
            try:
                data=Clients.objects.get(id=pk)
            except:
                return Response({'client': 'Not found'})
            serializer=ClientsSerializer(data,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)

    def delete(self,request,pk=None,*args,**kwargs):
        if pk is not None:
            try:
                data=Clients.objects.get(id=pk)
            except:
                return Response({'client': 'Not found'})
            if data.delete():
                return Response(status.HTTP_204_NO_CONTENT)
            else:
                return Response("Data not deleted")
        else:
            return Response("Invalid Id")


class Project(APIView):
    def get(self,request,pk=None,*args,**kwargs):
        if pk is not None:
            try:
                data=Projects.objects.get(id=pk)
            except:
                return Response({'project': 'Not found'})
            serializer=ProjectsSerializer(data)
            return Response(serializer.data)
        else:
            data=Projects.objects.all()
            serializer=ProjectsSerializer(data,many=True)
            return Response(serializer.data)


class User(APIView):
    def get(self,request,pk=None,*args,**kwargs):
        if pk is not None:
            data=Users.objects.get(id=pk)
            serializer=UserSerializer(data)
            return Response(serializer.data)
        else:
            data=Users.objects.all()
            serializer=UserSerializer(data,many=True)
            return Response(serializer.data)






