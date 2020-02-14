from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('courses-api/', include('courses.urls')),

    path('courses/', views.get_student_courses),
    path('lessons/', views.get_course_lessons),
    path('questions/', views.get_lesson_details),

    path('take-lesson/', views.take_lesson)
]
