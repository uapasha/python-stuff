from django.shortcuts import render
from django.core import serializers
from django.http import (HttpResponseBadRequest,
                        JsonResponse,
                        HttpResponse)
from django.views.decorators.csrf import csrf_exempt
from random import choice

from jobs.models import Job
from persons.models import Person

# Create your views here.
@csrf_exempt
def persons_json_list(request):
    if request.method != 'GET':
        return HttpResponseBadRequest('You can only use GET')
    else:
        persons = serializers.serialize('json', Person.objects.all(), 
                                        fields = ("short_name", 
                                                "full_name", 
                                                "email", 
                                                "job", 
                                                "colleagues"))

        return JsonResponse(persons, safe = False)

@csrf_exempt
def add_person(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('You can only use POST')
    else:
        short_name = request.POST['name']
        full_name = request.POST['full_name']
        email = request.POST['email']
        job = choice(Job.objects.all())
        new_person = Person(short_name = short_name, 
                            full_name = full_name, 
                            email = email, 
                            job = job)
        new_person.save()
        return HttpResponse('new person "%s" is added' % 
                        Person.objects.get(short_name = short_name).short_name)

@csrf_exempt
def delete_person(request, substr):
    if request.method != "DELETE":
        return HttpResponseBadRequest('You can only use DELETE')
    else:
        pers_to_del = Person.objects.filter(short_name__icontains = substr)
        num_persons = len(pers_to_del)
        pers_to_del.delete()
        return HttpResponse('succesfulye deleted %s persons' % num_persons)

