from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),



    path('course/create/', views.create_course, name='create_course'),
    path('course/read/', views.read_course, name='read_course'),
    path('course/update/', views.update_course, name='update_course'),
    path('course/create/', views.delete_course, name='delete_course'),

    path('lesson/create/', views.create_lesson, name='create_lesson'),
    path('lesson/read/', views.read_lesson, name='read_lesson'),
    path('lesson/update/', views.update_lesson, name='update_lesson'),
    path('lesson/delete/', views.delete_lesson, name='delete_lesson'),

    path('question/create/', views.create_question, name='create_question'),
    path('question/read/', views.read_question, name='read_question'),
    path('question/update/', views.update_question, name='update_question'),
    path('question/delete/', views.delete_question, name='delete_question'),
]
