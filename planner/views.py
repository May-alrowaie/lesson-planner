from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def classroom_index(request):
    return render(request, 'classrooms/index.html', {'classrooms': classrooms})


class Classroom:
    def __init__(self, subject_id, grade, division, students, feedback):
        self.subject_id = subject_id
        self.grade = grade
        self.division = division
        self.students = students  
        self.feedback = feedback  

classrooms = [
    Classroom(102, 'Grade 10', 'A', ['Aysha', 'Nuha', 'Salma'], 'Great participation.'),
    Classroom(102, 'Grade 11', 'B', ['Jood', 'Layla', 'Fiona'], 'Needs improvement in discipline.'),
    Classroom(317, 'Grade 12', 'A', ['Khadija', 'Hannah', 'Rima'], 'Excellent teamwork.'),
    Classroom(316, 'Grade 10', 'C', ['Mona', 'Reem', 'Hala'], 'Struggles with assignments.')
]

