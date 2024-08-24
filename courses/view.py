from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from .models import Course, Student, Teacher

# Create your views here.
def index(request):
    courses = get_list_or_404(Course)

    context = {
        'courses': courses
    }

    return render(request, 'courses/index.html', context)

def course_detail(request, course_id):
    
    course = get_object_or_404(Course, pk=course_id)
    response = 'Estas viendo el curso "%s"'
    
    return HttpResponse(response % course.name)

def students(request):
    students = get_list_or_404(Student)

    context = {'students': students}

    return render(request, 'courses/students.html', context)

def teachers(request):
    teachers = get_list_or_404(Teacher)

    context = {'teachers': teachers}

    return render(request, 'courses/teacher.html', context)
