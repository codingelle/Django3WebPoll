from django.contrib import admin

from .models import Question, Choice
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ('question_text', 'pub_date')
    list_display_links = ('pub_date',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
