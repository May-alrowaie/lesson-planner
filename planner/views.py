from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>Hello Teachers </h1>')

def about(request):
    return HttpResponse("<h1>About the Lesson planner app</h1>")
