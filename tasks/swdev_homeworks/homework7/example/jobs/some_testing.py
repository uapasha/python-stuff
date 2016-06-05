# -*- coding: utf-8 -*-
from urllib import request
import os
import django
import json
from sys import path as sys_path


# set django env
sys_path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")
django.setup()
from jobs.models import Job, FilteredJobsWrapper
from persons.models import Person, update_jobs

# url = 'http://standards.openprocurement.org/classifiers/dk003/uk.json'

# with request.urlopen(url) as url_data:
#     data = url_data.read().decode('utf-8')
#     data = json.loads(data)
#     l = [s for s in data.keys() if len(s) > 4]
#     s = set()
#     for i in l:
#         last = i.split('.')[-1]
#         s.add(last)
#     print (s)

# jobs = Job.objects.values('code').all()
# print (len(jobs))
# for i in range(len(jobs)):
#     print (jobs[i]['code'])

# f = FilteredJobsWrapper(12)
# for i in range(100):
#     s = next(f)
#     #print (s)

update_jobs()

