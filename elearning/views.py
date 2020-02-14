from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from courses.models import Course, Lesson, Question, StudentLesson
from courses.serializers import CourseSerializer, LessonSerializer, QuestionSerializer


def index(request):
    return JsonResponse({'foo': 'https://g.co'})


@api_view(['GET'])
def get_student_courses(request):
    """
    List all available student courses
    """
    courses = Course.objects.all()
    """
    TODO filter courses by the progress of the student
    """
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_course_lessons(request):
    """
    List all lessons of a course
    """
    course_id = request.GET.get("course", None)
    lessons = Lesson.objects.all()
    if course_id:
        lessons = lessons.filter(course_id=int(course_id))
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_lesson_details(request):
    """
    List all questions of a lesson
    """
    lesson_id = request.GET.get("lesson", None)
    questions = Question.objects.all()
    if lesson_id:
        questions = questions.filter(lesson_id=int(lesson_id))
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def take_lesson(request):
    """
    Save all questions of a lesson
    """
    lesson_id = request.POST.get("lesson", None)
    print(lesson_id)
    print(request.user.id)
    student_lesson = StudentLesson.objects.get_or_create(user_id=request.user.id, lesson_id=int(lesson_id))
    """
    TODO logic for verifying answers
    """
    student_lesson.score = 100
    student_lesson.is_passed = True
    student_lesson.save()
    return JsonResponse({'is_passed': True, "score":100})
