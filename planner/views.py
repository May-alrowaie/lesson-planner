from django.shortcuts import render , get_object_or_404, redirect
# from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Classroom , LessonPlan , Student , User 
from django.contrib.auth.views import LoginView 


class Home(LoginView):
    template_name = 'home.html'
    # success_url = 'home.html'


# def home(request):
#     return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#CLASSROOMS:

class ClassroomCreate(CreateView):
    model = Classroom
    fields = ['grade', 'division', 'students_list', 'feedback']
    # fields = '__all__'
    # success_url = '/classrooms/classroom_detail.html'

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)    


class ClassroomUpdate(UpdateView):
    model = Classroom
    fields = ['grade', 'division', 'students_list', 'feedback']
    # success_url = '/classrooms/'


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

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)    
    

class LessonPlanUpdate(UpdateView):
    model = LessonPlan
    fields = '__all__'
    # success_url = '/lessonplans/'

    
class LessonPlanDelete(DeleteView):
    model = LessonPlan
    success_url = '/lessonplans/'

#STUDENTS:

def student_index(request):
    students = Student.objects.all()     #  //
    return render(request, 'students/index.html', {'students': students}) 

def student_detail(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    return render(request, 'students/student_detail.html', {'student': student})

class StudentCreate(CreateView):
    model = Student
    fields = '__all__'
    success_url = '/students/'
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)        
    

class StudentUpdate(UpdateView):
    model = Student
    fields = '__all__'
    success_url = '/students/'

    
class StudentDelete(DeleteView):
    model = Student
    success_url = '/students/'

###???
print("Views.py is being loaded!") 
from planner.views import Home
