from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
	"""docstring for ChoiceInline"""
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	"""docstring for QuestionAdmin"""
	fieldsets = [
		('Enter text fot your Question', {'fields' : ['question_text']}),
		('Date information', {
			'fields':['pub_date'], 'classes': ['collapse']
			}),
	]
	
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']

	search_fields = ['question_text', 'pub_date']
	
	inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
		