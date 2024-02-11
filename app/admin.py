from django.contrib import admin

# Register your models here.

from app.models import *

class cust(admin.ModelAdmin):
    list_display = ['Sname','sprinc','sloc']

admin.site.register(School,cust)