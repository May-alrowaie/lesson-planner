from django.urls import path 
# ,include
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('classrooms/', views.classroom_index, name='classroom-index'),
path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),
path('classrooms/create/', views.ClassroomCreate.as_view(), name='classroom-create'),
path('classrooms/<int:pk>/update/', views.ClassroomUpdate.as_view(), name='classroom-update'),
path('classrooms/<int:pk>/delete/', views.ClassroomDelete.as_view(), name='classroom-delete'),

]

