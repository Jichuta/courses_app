from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from ..models import Teacher

@login_required
def teachers(request):
    try:
        teachers = get_list_or_404(Teacher)
    except:
        teachers = []    

    context = {'teachers': teachers}

    return render(request, 'courses/teacher.html', context)

@login_required
def save_teacher(request):
    try:
        teacher = Teacher(
            name=request.POST['name'],
            ci=request.POST['ci'],
            age=request.POST['age'],
            username=request.POST['username']
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

@login_required    
def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        teacher.delete()
        return redirect('courses:teacher')  # Redirect after deletion
    return render(request, 'courses/delete_teacher.html', {'teacher': teacher})     