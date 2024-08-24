from django.shortcuts import render, redirect
from ..models import Teacher, Course

def add_course(request):
    if request.method == 'POST':
        name = request.POST['name']
        teacher_id = request.POST['teacher']
        start_date = request.POST['start_date']

        try:
            teacher = Teacher.objects.get(id=teacher_id)
            course = Course(name=name, teacher=teacher, start_date=start_date)
            course.save()
            return redirect('courses:index')
        except Exception as e:
            context = {
                'teachers': Teacher.objects.all(),
                'error_message': 'An error occurred while saving the course: {}'.format(str(e))
            }
            return render(request, 'courses/course.html', context)
    else:
        context = {
            'teachers': Teacher.objects.all()
        }
        return render(request, 'courses/course.html', context)
