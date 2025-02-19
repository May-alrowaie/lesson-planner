from django.shortcuts import render , get_object_or_404, redirect
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Classroom , LessonPlan , Student 
from django.contrib.auth.views import LoginView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class Home(LoginView):
    template_name = 'home.html'
    # success_url = 'home.html'


# def home(request):
#     return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#CLASSROOMS:


class ClassroomCreate(LoginRequiredMixin,CreateView):
    model = Classroom
    fields = ['grade', 'division', 'students_list', 'feedback', 'user']
    # fields = '__all__'
    # success_url = '/classrooms/classroom_detail.html'

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)
    

class ClassroomUpdate(LoginRequiredMixin, UpdateView):
    model = Classroom
    fields = ['grade', 'division', 'students_list', 'feedback', 'user']
    # success_url = '/classrooms/'


class ClassroomDelete(LoginRequiredMixin,DeleteView):
    model = Classroom
    success_url = '/classrooms/'

@login_required
def classroom_index(request):
    # classrooms = Classroom.objects.all()    
    classrooms = Classroom.objects.filter(user=request.user)
    return render(request, 'classrooms/index.html', {'classrooms': classrooms})  

@login_required
def classroom_detail(request, classroom_id):
    classroom = get_object_or_404(Classroom, classroom_id=classroom_id)
    return render(request, 'classrooms/classroom_detail.html', {'classroom': classroom})

#LESSONPLANS:

@login_required
def lessonplan_index(request):
    # lessonplans = LessonPlan.objects.all()
    lessonplans = LessonPlan.objects.filter(user=request.user)
    return render(request, 'lessonplans/index.html', {'lessonplans': lessonplans})

@login_required
def lessonplan_detail(request, plan_id):
    lessonplan = LessonPlan.objects.get(plan_id=plan_id)
    return render(request, 'lessonplans/lessonplan_detail.html', {'lessonplan': lessonplan})


class LessonPlanCreate(LoginRequiredMixin, CreateView):
    model = LessonPlan
    fields = '__all__'
    success_url = '/lessonplans/'

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)    
    

class LessonPlanUpdate(LoginRequiredMixin, UpdateView):
    model = LessonPlan
    fields = '__all__'
    # success_url = '/lessonplans/'

    
class LessonPlanDelete(LoginRequiredMixin, DeleteView):
    model = LessonPlan
    success_url = '/lessonplans/'

#STUDENTS:
@login_required
def student_index(request):
    # students = Student.objects.all()     
    students = Student.objects.filter(user=request.user)
    return render(request, 'students/index.html', {'students': students}) 

@login_required
def student_detail(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    return render(request, 'students/student_detail.html', {'student': student})

class StudentCreate(LoginRequiredMixin, CreateView):
    model = Student
    fields = '__all__'
    success_url = '/students/'


    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)        
    

class StudentUpdate(LoginRequiredMixin, UpdateView):
    model = Student
    fields = '__all__'
    success_url = '/students/'

    
class StudentDelete(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = '/students/'



#signup:
def signup(request):
    error_message = ''
    if request.method == 'POST':
        
        form = UserCreationForm(request.POST)
        if form.is_valid():

            user = form.save()

            login(request, user)
            return redirect('classroom-index')
        
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    