from django.urls import path
from .views import (
    get_courses,
    get_students,
    get_payments,
    TrainingCourseListCreateAPI,
    StudentDetailsListCreateAPI,
    StudentPaymentListCreateAPI
)

urlpatterns = [
    path("courses/", get_courses),
    path("students/", get_students),
    path("payments/", get_payments),

    path("courses-api/", TrainingCourseListCreateAPI.as_view()),
    path("students-api/", StudentDetailsListCreateAPI.as_view()),
    path("payments-api/", StudentPaymentListCreateAPI.as_view()),
]