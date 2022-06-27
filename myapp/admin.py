from django.contrib import admin
from .models import todo
# Register your models here.
class TODOMODEL(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'user',
        'date',
        'Work_Status',
    )
admin.site.register(todo,TODOMODEL)
