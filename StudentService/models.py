from django.db import models


class TrainingCourse(models.Model):
    CourseId = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=100)
    CourseFees = models.DecimalField(max_digits=10, decimal_places=2)
    GST = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = "tbl_training_courses"

    def __str__(self):
        return self.CourseName


class StudentDetails(models.Model):
    StudentId = models.AutoField(primary_key=True)
    StudentName = models.CharField(max_length=100)
    EmailAddress = models.CharField(max_length=100)
    MobileNumber = models.CharField(max_length=20)
    City = models.CharField(max_length=50)
    Course = models.ForeignKey(TrainingCourse, on_delete=models.CASCADE)
    Discount = models.DecimalField(max_digits=10, decimal_places=2)
    RegistrationDate = models.DateField()

    class Meta:
        db_table = "tbl_student_details"

    def __str__(self):
        return self.StudentName


class StudentPayment(models.Model):
    PaymentId = models.AutoField(primary_key=True)
    Student = models.ForeignKey(StudentDetails, on_delete=models.CASCADE)
    PaymentDate = models.DateField()
    PaymentAmount = models.DecimalField(max_digits=10, decimal_places=2)
    PaymentMode = models.CharField(max_length=30)
    PaymentDescription = models.CharField(max_length=200)

    class Meta:
        db_table = "tbl_student_payments"

    def __str__(self):
        return f"{self.Student.StudentName} - {self.PaymentAmount}"