from django.contrib import admin
from crud.models import rform


class rformAdmin(admin.ModelAdmin):
    list=('fname','lname','dob','gender','file')


admin.site.register(rform,rformAdmin)
# Register your models here.
