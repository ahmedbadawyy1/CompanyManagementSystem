from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, ProjectViewSet, EmployeeViewSet, TaskViewSet , ExpenseViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'expense', ExpenseViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
