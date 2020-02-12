from rest_framework import serializers

from courses.models import Question, Lesson, Course


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['id','name', 'approval_score', 'dependencies']


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'course', 'approval_score', 'dependencies']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'score', 'type', 'lesson']
