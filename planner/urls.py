from django.urls import path 
# ,include
from . import views

urlpatterns = [
path('', views.home, name='home'),
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
]

