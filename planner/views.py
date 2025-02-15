from django.shortcuts import render , get_object_or_404, redirect
# from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView   
from .models import Classroom , LessonPlan , Student , User


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

 #CLASSROOMS:

class ClassroomCreate(CreateView):
    model = Classroom
    fields = ['grade', 'division', 'students_list', 'feedback']
    # fields = '__all__'
    # success_url = '/classrooms/'
    


class ClassroomUpdate(UpdateView):
    model = Classroom
    fields = ['grade', 'division', 'students_list', 'feedback']
    success_url = '/classrooms/'

    
class ClassroomDelete(DeleteView):
    model = Classroom
    success_url = '/classrooms/'


def classroom_index(request):
    classrooms = Classroom.objects.all()     #  //
    return render(request, 'classrooms/index.html', {'classrooms': classrooms})  

def classroom_detail(request, classroom_id):
    classroom = get_object_or_404(Classroom, classroom_id=classroom_id)
    return render(request, 'classrooms/classroom_detail.html', {'classroom': classroom})

#LESSONPLANS:

def lessonplan_index(request):
    lessonplans = LessonPlan.objects.all()
    return render(request, 'lessonplans/index.html', {'lessonplans': lessonplans})

def lessonplan_detail(request, plan_id):
    lessonplan = LessonPlan.objects.get(plan_id=plan_id)
    return render(request, 'lessonplans/lessonplan_detail.html', {'lessonplan': lessonplan})


class LessonPlanCreate(CreateView):
    model = LessonPlan
    fields = '__all__'
    success_url = '/lessonplans/'
    

class LessonPlanUpdate(UpdateView):
    model = LessonPlan
    fields = '__all__'
    success_url = '/lessonplans/'

    
class LessonPlanDelete(DeleteView):
    model = LessonPlan
    success_url = '/lessonplans/'

    
