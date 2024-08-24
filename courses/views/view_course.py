from django.shortcuts import render, redirect, get_object_or_404
from ..models import Teacher, Course

def add_course(request):
    if request.method == 'POST':
        name = request.POST['name']
        teacher_id = request.POST['teacher']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        state = request.POST['state']
        material_curso = request.POST['material_curso']

        try:
            teacher = Teacher.objects.get(id=teacher_id)
            course = Course(name=name, teacher=teacher, start_date=start_date,
                            end_date=end_date, state=state, material_curso=material_curso)
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

def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('courses:index')  # Redirect after deletion
    return render(request, 'courses/delete_course.html', {'course': course})    
