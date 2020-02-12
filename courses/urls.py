from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from courses.views import QuestionViewSet, LessonViewSet, CourseViewSet

router = routers.DefaultRouter()

router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
