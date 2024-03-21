from .models import Person
from .serializers import PersonSerialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PersonView(APIView):
    def get(self, request):
        people = Person.objects.all() 
        serialize = PersonSerialize(people, many=True)
        return Response(serialize.data)
    def post(self, request):
        serialize = PersonSerialize(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Doen'})


class PersonDetail(APIView):
    def get_by_pk(self, id):
        try:
            return Person.objects.get(pk=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
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
        serialize = PersonSerialize(person, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def pust(self, request, id):
        person = self.get_by_pk(id)
        serialize = PersonSerialize(person, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)