from django import forms
from persons.models import UserProfile, Person
from jobs.models import Job
from django.contrib.auth.models import User

class AddPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('short_name', 'full_name', 'email', 'job', 'colleagues')
    # short_name = forms.CharField(max_length=32, required=True)
    # full_name = forms.CharField(max_length=128, required=False)
    # email = forms.EmailField(max_length=128, required=False)
    # job = forms.ModelChoiceField(Job.objects, required= True)

class RemovePersonForm(forms.Form):
    short_name_substr = forms.CharField(max_length=32, required=True)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class EditPerson(forms.ModelForm):
    class Meta:
     model = Person
     fields = '__all__'
