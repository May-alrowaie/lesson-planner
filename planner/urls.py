from django.urls import path
from django.contrib import admin
from . import views
from .views import Home  
import planner.views as views  
urlpatterns = [
    path('', Home.as_view(), name='home'),
    # path('', views.Home.as_view(), name='home'),

    # path('', views.home, name='home'),
    path('about/', views.about, name='about'),

#urls for classrooms:

    path('classrooms/', views.classroom_index, name='classroom-index'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    #CRUD urls for classrooms:
    path('classrooms/create/', views.ClassroomCreate.as_view(), name='classroom-create'),
    path('classrooms/<int:pk>/update/', views.ClassroomUpdate.as_view(), name='classroom-update'),
    path('classrooms/<int:pk>/delete/', views.ClassroomDelete.as_view(), name='classroom-delete'),

    #urls for lessonplans:
    path('lessonplans/', views.lessonplan_index, name='lessonplan-index'),
    path('lessonplans/<int:plan_id>/', views.lessonplan_detail, name='lessonplan-detail'),

    #CRUD urls for lessonplans:
    path('lessonplans/create/', views.LessonPlanCreate.as_view(), name='lessonplan-create'),
    path('lessonplans/<int:pk>/update/', views.LessonPlanUpdate.as_view(), name='lessonplan-update'),
    path('lessonplans/<int:pk>/delete/', views.LessonPlanDelete.as_view(), name='lessonplan-delete'),

    #urls for students:
    path('students/', views.student_index, name='student-index'),
    path('students/<int:student_id>/', views.student_detail, name='student-detail'),

    #CRUD urls for students:
    path('students/create/', views.StudentCreate.as_view(), name='student-create'),
    path('students/<int:pk>/update/', views.StudentUpdate.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', views.StudentDelete.as_view(), name='student-delete'),

    path('accounts/signup/', views.signup, name='signup'),


]

