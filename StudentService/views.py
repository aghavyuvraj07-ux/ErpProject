from django.http import JsonResponse
from rest_framework import generics
from .models import TrainingCourse, StudentDetails, StudentPayment
from .serializers import (
    TrainingCourseSerializer,
    StudentDetailsSerializer,
    StudentPaymentSerializer
)


def get_courses(request):
    courses = TrainingCourse.objects.all()

    data = []

    for course in courses:
        data.append({
            "CourseId": course.CourseId,
            "CourseName": course.CourseName,
            "CourseFees": str(course.CourseFees),
            "GST": str(course.GST)
        })

    return JsonResponse(data, safe=False)


def get_students(request):
    students = StudentDetails.objects.all()

    data = []

    for student in students:
        data.append({
            "StudentId": student.StudentId,
            "StudentName": student.StudentName,
            "EmailAddress": student.EmailAddress,
            "MobileNumber": student.MobileNumber,
            "City": student.City,
            "Course": student.Course.CourseName,
            "Discount": str(student.Discount),
            "RegistrationDate": student.RegistrationDate
        })

    return JsonResponse(data, safe=False)


def get_payments(request):
    payments = StudentPayment.objects.all()

    data = []

    for payment in payments:
        data.append({
            "PaymentId": payment.PaymentId,
            "Student": payment.Student.StudentName,
            "PaymentDate": payment.PaymentDate,
            "PaymentAmount": str(payment.PaymentAmount),
            "PaymentMode": payment.PaymentMode,
            "PaymentDescription": payment.PaymentDescription
        })

    return JsonResponse(data, safe=False)


class TrainingCourseListCreateAPI(generics.ListCreateAPIView):
    queryset = TrainingCourse.objects.all()
    serializer_class = TrainingCourseSerializer


class StudentDetailsListCreateAPI(generics.ListCreateAPIView):
    queryset = StudentDetails.objects.all()
    serializer_class = StudentDetailsSerializer


class StudentPaymentListCreateAPI(generics.ListCreateAPIView):
    queryset = StudentPayment.objects.all()
    serializer_class = StudentPaymentSerializer