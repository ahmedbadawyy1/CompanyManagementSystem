from django.contrib import admin
from .models import Employee, Expense,Task,Department,Project
# Register your models here.


# to make this models apear in admin panel
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Expense)

