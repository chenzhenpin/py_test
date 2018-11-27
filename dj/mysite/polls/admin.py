from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *


class QuestionAdmin(ModelAdmin):
    list_display = ('question_text','pub_date')
    fields = ('pub_date', )
    list_filter = ('pub_date',)
    search_fields = ('question_text',)
    class Meta:
        verbose_name='问题'




class ChoiceAdmin(ModelAdmin):
    list_display = ('choice_text','votes')
    list_editable = ('votes',)


# Register your models here.
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
