from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, Http404
from ..models import Student

def students(request):
    students = get_list_or_404(Student)

    context = {'students': students}

    return render(request, 'courses/students.html', context)

def save_student(request):
    try:
        student = Student(
            name=request.POST['name'],
            ci=request.POST['ci'],
            username=request.POST['username'],
        )
        student.save()
        return redirect('courses:students')
    except Exception:
        students = get_list_or_404(Student)
        context = {
            'students': students,
            'error_message': 'Huvo un error'
        }
        return render(request, 'courses/students.html', context)