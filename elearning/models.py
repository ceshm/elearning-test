from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    aproval_score = models.IntegerField(max_length=3)
    is_aproved = models.BooleanField()


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    is_passed = models.BooleanField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


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
