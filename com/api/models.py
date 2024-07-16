from django.db import models


# model for departments 
class Department(models.Model):
    name = models.CharField(max_length=150, verbose_name="dep_name")
    description = models.CharField(max_length=500, verbose_name="dep_desc", blank=True, null=True)
   
    def __str__(self):
        return self.name


# model for project 
class Project(models.Model):
    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    name = models.CharField(max_length=200, verbose_name="proj_name")
    description = models.CharField(max_length=500, verbose_name="proj_desc", blank=True, null=True)
    start_date = models.DateField(verbose_name="proj_start")
    end_date = models.DateField(verbose_name="proj_deadline")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Started', verbose_name="proj_status")
    department = models.ForeignKey(Department,on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.name

# model for employees 
class Employee(models.Model):
    name = models.CharField(max_length=150, verbose_name="emp_name")
    email = models.EmailField(max_length=300, verbose_name="emp_email")
    age = models.IntegerField(verbose_name="emp_age")
    job_name = models.CharField(max_length=150, verbose_name="emp_position")
    phone = models.CharField(max_length=13, verbose_name="emp_phone")
    hire_date = models.DateField()
    department = models.ForeignKey(Department,  on_delete=models.SET_NULL, related_name='assigned_to',null=True, blank=True)

    def __str__(self):
        return self.name
    
# model for tasks 
class Task(models.Model):
    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    name = models.CharField(max_length=200, verbose_name="task_name")
    description = models.CharField(max_length=500, verbose_name="task_desc", blank=True, null=True)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='tasks')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="task_project", related_name='tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Started', verbose_name="task_status")
    due_date = models.DateField()

    def __str__(self):
        return self.name
    
#model for expense 
class Expense(models.Model):
        STATUS_CHOICES = [
        ('approved', 'approved'),
        ('Pending', 'Pending'),
        ('NotApproved', 'NotApproved'),
    ]
        name = models.CharField(max_length= 250,  verbose_name="expense_name")
        description = models.CharField(max_length=500, verbose_name="expense_desc", blank=True, null=True)   
        assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='expense')
        project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="expense_project", related_name='expense')
        status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending', verbose_name="expense_status")
        due_date = models.DateField() 

        def __str__(self) :
            return self.name
   
