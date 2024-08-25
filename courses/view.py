from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from .models import Course, Student, Teacher

# Create your views here.
def index(request):
    try:
        courses = get_list_or_404(Course)
    except:
        courses = []

    user_role = request.session.get('user_role')
    user_name = request.session.get('username')

    if user_role == 'profesor':
        courses = [course for course in courses if course.teacher.username == user_name]

    context = {
        'courses': courses
    }

    return render(request, 'courses/index.html', context)

def course_detail(request, course_id):
    
    course = get_object_or_404(Course, pk=course_id)
    response = 'Estas viendo el curso "%s"'
    
    return HttpResponse(response % course.name)

def students(request):
    try:
        students = get_list_or_404(Student)
    except:
        students = []    

    context = {'students': students}

    return render(request, 'courses/students.html', context)

def teachers(request):
    try:
        teachers = get_list_or_404(Teacher)
    except:
        teachers = []   

    context = {'teachers': teachers}

    return render(request, 'courses/teacher.html', context)
