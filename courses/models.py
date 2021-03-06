from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    approval_score = models.IntegerField()
    dependencies = models.ManyToManyField("Course", null=True, blank=True)

    def __str__(self):
        return self.name


class StudentCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    approval_score = models.IntegerField()
    dependencies = models.ManyToManyField("Lesson", null=True, blank=True)

    def __str__(self):
        return self.name


class StudentLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    is_passed = models.BooleanField(default=False)


class Question(models.Model):
    BOOLEAN = 'BL'
    MULTI_1 = 'M1'
    MULTI_M = 'MM'
    MULTI_C = 'MC'
    QUESTION_TYPE_CHOICES = [
        (BOOLEAN, 'Boolean'),
        (MULTI_1, 'Multiple choice where only one answer is correct'),
        (MULTI_M, 'Multiple choice where more than one answer is correct'),
        (MULTI_C, 'Multiple choice where more than one answer is correct and all of them must be answered correctly'),
    ]
    text = models.TextField()
    score = models.IntegerField(max_length=3)
    type = models.CharField(max_length=2, choices=QUESTION_TYPE_CHOICES, default=BOOLEAN)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.text