from .models import Person
from .serializers import PersonSerialize
from django.views import View
from rest_framework.response import Response


class PersonView(View):
    def get(self, request):
        people = Person.objects.all() 
        serialize = PersonSerialize(people, many=True)
        return Response(serialize.data)
