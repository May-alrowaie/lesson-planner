from django.contrib import admin

from .models import Classroom , LessonPlan , Student 

admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(LessonPlan)

