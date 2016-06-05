from random import choice

from django.db import models

from django.contrib.auth.models import User

from jobs.models import Job, FilteredJobsWrapper

class Person(models.Model):
    short_name = models.CharField(max_length=32, unique=True, null=False,
                                    blank=False)
    full_name = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(max_length=128, null=True, blank=True)

    job = models.ForeignKey(Job, verbose_name = 'Job description')

    colleagues = models.ManyToManyField("self", blank=True, null=True)

    def __str__(self):
        return '%s%s' % (self.short_name,
                          ' (%s)' % self.full_name if self.full_name else '')

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

def update_jobs(code_digit_sum = 8, random = False):
    if not random:
        new_job = FilteredJobsWrapper(code_digit_sum)
        for p in Person.objects.all():
            try:
                new_job_code = next(new_job)
            except StopIteration:
                new_job = FilteredJobsWrapper(code_digit_sum)
                new_job_code = next(new_job)
            new_job_obj = Job.objects.get(code = new_job_code)
            p.job = new_job_obj
            p.save()
    else:
        for p in Person.objects.all():
            new_job = choice(Job.objects.all())
            p.job = new_job
            p.save()



