# -*- coding: utf-8 -*-

from django.db import models
import uuid

# Create your models here.

class Job(models.Model):
    code = models.CharField(unique=True, max_length = 20)
    description = models.CharField('job description', max_length = 255)

    def __str__ (self):
        if len(self.description) > 99:
            return ('%s' + '...') % (self.description[:100])
        else:
            return '%s' % (self.description)

def sum_digits(code):
    sum = 0
    for i in code:
        try:
            i = int(i)
            sum += i
        except ValueError:
            pass
    return sum

class FilteredJobsWrapper():
    def __init__(self, code_digit_sum):
        assert code_digit_sum >= 5
        assert code_digit_sum <= 15
        self.code_digit_sum = code_digit_sum
        self.elem = 0
        self.job_codes = Job.objects.values('code').all()

    def __iter__(self):
        return self

    def __next__(self):

        while self.elem  < len(self.job_codes) - 1:
            self.elem +=1
            code = self.job_codes[self.elem]['code']

            if sum_digits(code) == self.code_digit_sum:
                return code
        raise StopIteration