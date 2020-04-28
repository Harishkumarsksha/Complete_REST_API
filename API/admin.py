from django.contrib import admin

# Register your models here.
from API.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('eno', 'ename', 'esal', 'eaddr', 'eemail',)
    list_filter = ('eno', 'ename', 'eemail',)
    search_fields = ('eno', 'ename', 'eaddr', 'eemail',)


admin.site.register(Employee, EmployeeAdmin)
