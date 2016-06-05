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

from jobs.models import Job

url = 'http://standards.openprocurement.org/classifiers/dk003/uk.json'

with request.urlopen(url) as url_data:
    data = url_data.read().decode('utf-8')
    data = json.loads(data)
    jobs_added = 0
    for k in data:
        new_job = Job(code = k, description = data[k])
        new_job.save()
        jobs_added +=1 
    print ('succesfully imported %s jobs' % jobs_added)




# with open('jobs/uk.json' , 'r') as data:
#     data = data.read()
#     data = json.loads(data)
#     for k in data:
#         print (data[k])
#     print(len(max(data.keys(), key = len)))
#     print(len(max(data.values(), key = len)))

    # s = 'Професіонали в сфері державної служби, аудиту, \
    # бухгалтерського обліку, праці та зайнятості, маркетингу, \
    # ефективності підприємництва,\
    # раціоналізації виробництва та інтелектуальної власності'
    # print (s[:10000])
