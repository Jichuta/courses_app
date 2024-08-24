from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, Http404
from ..models import Teacher

def teachers(request):
    teachers = get_list_or_404(Teacher)

    context = {'teachers': teachers}

    return render(request, 'courses/teacher.html', context)

def save_teacher(request):
    try:
        teacher = Teacher(
            name=request.POST['name'],
            ci=request.POST['ci'],
            age=request.POST['age']
        )
        teacher.save()
        return redirect('courses:teacher')
    except Exception:
        teachers = get_list_or_404(Teacher)
        context = {
            'teacher': teachers,
            'error_message': 'Huvo un error'
        }
        return render(request, 'courses/teacher.html', context)