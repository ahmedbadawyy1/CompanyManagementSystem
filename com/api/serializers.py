from rest_framework import serializers
from .models import Employee, Expense
from .models import Department
from .models import Task
from .models import Project



# Department Serializer 
class  DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','name','description']

# Project Serializer 
class  ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','name','description','start_date','end_date','status','department']

# Employee Serializer 
class  EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','name','email','age','job_name','phone','hire_date','department']


# Task Serializer 
class TaskSerializer(serializers.ModelSerializer):
    assigned_to_name = serializers.SerializerMethodField()
    project_name = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'assigned_to', 'assigned_to_name', 'project', 'project_name', 'status', 'due_date']

# زلازم اكتب get  علشان اعرف اجيب الاسم من idمن حته تانيه  

    def get_assigned_to_name(self, obj):
        return obj.assigned_to.name if obj.assigned_to else None

    def get_project_name(self, obj):
        return obj.project.name if obj.project else None


# Expense Serializer 
class ExpenseSerializer(serializers.ModelSerializer):
    assigned_to_name = serializers.SerializerMethodField()
    project_name = serializers.SerializerMethodField()
    class Meta:
        model = Expense 
        fields = ['id', 'name', 'description', 'assigned_to','assigned_to_name','project', 'project_name', 'status', 'due_date']  

    def get_assigned_to_name(self, obj):
        return obj.assigned_to.name if obj.assigned_to else None

    def get_project_name(self, obj):
        return obj.project.name if obj.project else None

# Serializer for updating expense status
class UpdateExpenseStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Expense.STATUS_CHOICES)