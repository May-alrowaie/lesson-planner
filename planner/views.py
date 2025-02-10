from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def classroom_index(request):
    return render(request, 'classrooms/index.html', {'classrooms': classrooms})  # Update this line why is has ss in classroom`


class Classroom:
    def __init__(self, subject_id, grade, division, students, feedback):
        self.subject_id = subject_id
        self.grade = grade
        self.division = division
        self.students = students  
        self.feedback = feedback  

classrooms = [
    Classroom(102, 'Grade 10', 'A', ['Aysha', 'Nuha', 'Salma'], 'Great participation.'),
    
]

def classroom_detail(request, classroom_id):
    classroom = Classroom.objects.get(id= classroom_id)
    return render(request, 'classrooms/detail.html', {'classroom': classroom})
# and this doesnt have ss in classroom