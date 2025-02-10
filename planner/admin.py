from django.contrib import admin

from .models import Classroom , LessonPlan , Student , User

admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(User)
admin.site.register(LessonPlan)

