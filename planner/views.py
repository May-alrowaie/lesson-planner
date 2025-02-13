from django.shortcuts import render 
# from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView    
from .models import Classroom


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


class ClassroomCreate(CreateView):
    model = Classroom
    fields = ['grade', 'division', 'students_list', 'feedback']
    success_url = '/classroom/'

class ClassroomUpdate(UpdateView):
    model = Classroom
    fields = ['grade', 'division', 'students_list', 'feedback']

class ClassroomDelete(DeleteView):
    model = Classroom
    success_url = '/classrooms/'


def classroom_index(request):
    classrooms = Classroom.objects.all()     #  //
    return render(request, 'classrooms/index.html', {'classrooms': classrooms})  # Update this line why is has ss in classroom`

def classroom_detail(request, classroom_id):
    classroom = Classroom.objects.get(id= classroom_id)
    return render(request, 'classrooms/detail.html', {'classroom': classroom})
# and this doesnt have ss in classroom



#hardcoded data for testing need to be removed

# class Classroom:
#     def __init__(self, grade, division, students_list, feedback):
#         self.grade = grade
#         self.division = division
#         self.students_list = students_list     # list of students i need to check if it is correct
#         self.feedback = feedback  




# classrooms = [
#     Classroom( 'Grade 10', 'A', ['Aysha', 'Nuha', 'Salma'], 'Great participation.'),
# ]

