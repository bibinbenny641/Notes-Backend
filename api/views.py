from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from.models import Notes
from.serialiezer import NotesSerializer

# Create your views here.

class Notes_view(APIView):
    def get(self,request,**kwrgs):
        print(kwrgs)

        if kwrgs:
            
            ob = Notes.objects.get(id=kwrgs['id'])
            
            serializer = NotesSerializer(ob,many=False)
            if serializer.is_valid:
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            
            ob = Notes.objects.all().order_by('-id')
            serializer = NotesSerializer(ob,many=True)
            if serializer.is_valid:
               return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    def post(self,request):
         data = request.data['data']
         print(data)
         no = Notes.objects.create(title = data['title'],body = data['note'])
         serializer = NotesSerializer(no,many=False)
         return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def put(self,request,id):
        data = request.data['data']
        print(data)
        edit = Notes.objects.get(id=id)
        if data['title']:
            edit.title = data['title']
            print('hi')
        if data['note']:

            edit.body = data['note']
            print('ho')
        edit.save() 
        
        return Response(status=status.HTTP_200_OK)

    def delete(self,request,id):
        print(id)
        print(request.data)
        ob = Notes.objects.get(id=id)
        print(ob.title)
        dataa = {'delete':'success'}
        ob.delete()
        return Response(dataa,status=status.HTTP_202_ACCEPTED)