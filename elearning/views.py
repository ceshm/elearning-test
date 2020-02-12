from django.http import JsonResponse
from rest_framework import viewsets



def index(request):
    return JsonResponse({'foo': 'https://g.co'})


def get_student_courses(request):
    return JsonResponse({'foo': 'bar'})

def get_course_lessons(request):
    return JsonResponse({'foo': 'bar'})

def get_lesson_details(request):
    return JsonResponse({'foo': 'bar'})

def take_a_lesson(request):
    return JsonResponse({'foo': 'bar'})


# Course CRUD
def create_course(request):
    return JsonResponse({'foo': 'bar'})

def read_course(request):
    return JsonResponse({'foo': 'bar'})

def update_course(request):
    return JsonResponse({'foo': 'bar'})

def delete_course(request):
    return JsonResponse({'foo': 'bar'})


# Lesson CRUD
def create_lesson(request):
    return JsonResponse({'foo': 'bar'})

def read_lesson(request):
    return JsonResponse({'foo': 'bar'})

def update_lesson(request):
    return JsonResponse({'foo': 'bar'})

def delete_lesson(request):
    return JsonResponse({'foo': 'bar'})


# Question CRUD

def create_question(request):
    return JsonResponse({'foo': 'bar'})

def read_question(request):
    return JsonResponse({'foo': 'bar'})

def update_question(request):
    return JsonResponse({'foo': 'bar'})

def delete_question(request):
    return JsonResponse({'foo': 'bar'})
