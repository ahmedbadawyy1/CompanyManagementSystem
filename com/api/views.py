from rest_framework import viewsets 
from .models import Department, Expense, Project, Employee, Task
from .serializers import DepartmentSerializer, ExpenseSerializer, ProjectSerializer, EmployeeSerializer, TaskSerializer, UpdateExpenseStatusSerializer
from rest_framework.decorators import action
from rest_framework.response import Response



# Viewset for Department
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# Viewset for Project
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# http://127.0.0.1:8000/api/projects/by-department/?department_id=2
# function to get all project for


    @action(detail=False, methods=['get'], url_path='by-department')
    def list_by_department(self, request):
        department_id = request.query_params.get('department_id')
        if department_id is not None:
            project = Project.objects.filter(department=department_id)
            serializer = self.get_serializer(project, many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "department ID not provided"}, status=400)

# Viewset for Employee
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Viewset for Task
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


#http://127.0.0.1:8000/api/tasks/by-employee/?employee_id=1
# function to get all tasks for employeee 
    @action(detail=False, methods=['get'], url_path='by-employee')
    def list_by_employee(self, request):
        employee_id = request.query_params.get('employee_id')
        if employee_id is not None:
            tasks = Task.objects.filter(assigned_to=employee_id)
            serializer = self.get_serializer(tasks, many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "Employee ID not provided"}, status=400)

## function to get all tasks for project 
    @action(detail=False, methods=['get'], url_path='by-project')
    def list_by_project(self, request):
        project_id = request.query_params.get('project_id')
        if project_id is not None:
            tasks = Task.objects.filter(project=project_id)
            serializer = self.get_serializer(tasks, many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "project ID not provided"}, status=400)
        
       
        

# Viewset for Expense
class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer   


#http://127.0.0.1:8000/api/expense/by-project/?project_id=2
## function to get all expense for project 
    @action(detail=False, methods=['get'], url_path='by-project')
    def list_by_project(self, request):
        project_id = request.query_params.get('project_id')
        if project_id is not None:
            expenses = Expense.objects.filter(project=project_id)
            serializer = self.get_serializer(expenses, many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "project ID not provided"}, status=400)     
        #http://127.0.0.1:8000/api/expense/{id}/update-status/
    # Function to update the status of an expense
    @action(detail=True, methods=['post'], url_path='update-status')
    def update_status(self, request, pk=None):
        expense = self.get_object()
        serializer = UpdateExpenseStatusSerializer(data=request.data)
        if serializer.is_valid():
            expense.status = serializer.validated_data['status']
            expense.save()
            return Response({'status': 'status updated'})
        else:
            return Response(serializer.errors, status=400)
        

        