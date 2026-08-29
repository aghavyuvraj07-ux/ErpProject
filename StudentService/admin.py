from django.contrib import admin
from .models import TrainingCourse, StudentDetails, StudentPayment


admin.site.register(TrainingCourse)
admin.site.register(StudentDetails)
admin.site.register(StudentPayment)