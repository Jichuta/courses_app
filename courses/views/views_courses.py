from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from ..models import Course, CourseStudent
from django.urls import reverse

# Create your views here.
def index(request):
    courses = get_list_or_404(Course)

    context = {
        'courses': courses
    }

    return render(request, 'courses/index.html', context)

def course_detail(request, course_id):
    encoded_role = request.session.get('user_role')
    print(">>>>>>> user_role >>>>>" + str(encoded_role))
    
    course = get_object_or_404(Course, pk=course_id)
    students = CourseStudent.objects.filter(course=course)

    response = '<h1>Curso "{}"</h1>'.format(course.name)
    response += '<h2>Lista de estudiantes registrados:</h2>'
    response += '<ul>'

    for cs in students:
        response += '<li>{} (CI: {}) - Nota: {} - Aprobado: {}</li>'.format(
            cs.student.name,
            cs.student.ci,
            cs.grade,
            'Sí' if cs.isApproved else 'No'
        )

    response += '</ul>'

    # Adding a button to add a new student to the course
    add_student_url = reverse('courses:add_course_student', args=[course.id])
    response += '<a href="{}"><button>Añadir nuevo estudiante</button></a>'.format(add_student_url)

    return HttpResponse(response)
