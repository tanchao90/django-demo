from django.contrib import admin

from .models import Question, Choice


# Register your models here.

class QuestionAdminOrder(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdminSet(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdminSet)
admin.site.register(Choice)
