from rest_framework import viewsets

from courses.models import Question, Course, Lesson
from courses.permissions import HasGroupPermission
from courses.serializers import QuestionSerializer, CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Professors',],
        'POST': ['Professors',],
        'PUT': ['Professors'],
    }
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonViewSet(viewsets.ModelViewSet):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Professors', ],
        'POST': ['Professors', ],
        'PUT': ['Professors'],
    }
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Professors', ],
        'POST': ['Professors', ],
        'PUT': ['Professors'],
    }
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
