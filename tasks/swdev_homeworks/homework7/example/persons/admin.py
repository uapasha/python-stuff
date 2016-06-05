from django.contrib import admin
from persons.models import Person, UserProfile
from jobs.models import Job

admin.site.register(Person)
admin.site.register(UserProfile)
admin.site.register(Job)