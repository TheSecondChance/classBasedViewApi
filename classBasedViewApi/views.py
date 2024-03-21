from .models import Person
from .serializers import PersonSerialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class PersonView(APIView):
    def get(self, request):
        people = Person.objects.all() 
        serializer = PersonSerialize(people, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PersonSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonDetail(APIView):
    def get_by_pk(self, id):
        try:
            return Person.objects.get(pk=id)
        except Person.DoesNotExist:
            raise Http404
    
    def get(self, request, id):
        person = self.get_by_pk(id)
        serializer = PersonSerialize(person)
        return Response(serializer.data)
    
    def delete(self, request, id):
        person = self.get_by_pk(id)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, id):
        person = self.get_by_pk(id)
        serializer = PersonSerialize(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def pust(self, request, id):
        person = self.get_by_pk(id)
        serializer = PersonSerialize(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)