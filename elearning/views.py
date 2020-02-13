from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from courses.models import Course
from courses.serializers import CourseSerializer


def index(request):
    return JsonResponse({'foo': 'https://g.co'})


def get_student_courses(request):


    return JsonResponse({'foo': 'bar'})


@api_view(['GET',])
def get_student_courses_2(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


def get_course_lessons(request):
    return JsonResponse({'foo': 'bar'})

def get_lesson_details(request):
    return JsonResponse({'foo': 'bar'})

def take_a_lesson(request):
    return JsonResponse({'foo': 'bar'})

