from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.


# CLASSROOM
class Classroom(models.Model):
    classroom_id = models.AutoField(primary_key=True)
    grade = models.CharField(max_length=10)
    division = models.CharField(max_length=10)
    students_list = models.TextField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # return self.name
        return f"{self.grade} - {self.division}"
    
    def get_absolute_url(self):
        return reverse('classroom-detail', kwargs={'classroom_id': self.classroom_id})
    
#LESSONPLAN   
class LessonPlan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lesson_plans')
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True, related_name='lesson_plans')
    subject_id = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    grade_level = models.CharField(max_length=10)
    division = models.CharField(max_length=10)
    duration = models.DurationField()
    date = models.DateField()
    objectives = models.TextField()
    integration = models.TextField(blank=True, null=True)
    teaching_strategy = models.TextField()
    description = models.TextField()
    activity_level = models.CharField(max_length=50)
    activities = models.TextField()
    assessment = models.TextField()
    technology_used = models.TextField(blank=True, null=True)
    plan_b = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='lesson_plans')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('lessonplan-detail', kwargs={'plan_id': self.plan_id})

#STUDENT   
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    division = models.CharField(max_length=10)
    student_level = models.CharField(max_length=50)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    activity_level = models.CharField(max_length=50)
    learning_style = models.CharField(max_length=50)
    multiple_intelligence = models.CharField(max_length=100)
    special_needs = models.TextField(blank=True, null=True)
    parent_info = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name
    
    # def get_absolute_url(self):
    #     return reverse('student-detail', kwargs={'student_id': self.student_id})

    def save(self, *args, **kwargs):

        if self.pk:
            old_student = Student.objects.get(pk=self.pk)  

            if old_student.classroom != self.classroom:
                old_classroom = old_student.classroom
                if old_classroom and old_classroom.students_list:
                    current_students = old_classroom.students_list.split(", ")
                    if self.name in current_students:
                        current_students.remove(self.name)  
                        old_classroom.students_list = ", ".join(current_students)
                        old_classroom.save()

        super().save(*args, **kwargs) 

        new_classroom = self.classroom
        if new_classroom:
            current_students = new_classroom.students_list.split(", ") if new_classroom.students_list else []
            if self.name not in current_students:  
                current_students.append(self.name)
                new_classroom.students_list = ", ".join(current_students)
                new_classroom.save()

   
    def __str__(self):
        return self.name
    
    