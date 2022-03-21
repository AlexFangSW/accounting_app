from django.contrib import admin
from .models import Record, Tag

# Register your models here.
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'income_or_expense', 'tag_name', 'discription', 'price', 'date')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'income_or_expense', 'tag_name')