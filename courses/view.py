from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from .models import Course, Student, Teacher, CourseStudent
from django.utils import timezone

# Create your views here.
def index(request):
    try:
        courses = get_list_or_404(Course)
    except:
        courses = []

    today = timezone.now().date() ## + timedelta(1)
    user_role = request.session.get('user_role')
    user_name = request.session.get('username')

    if user_role == 'profesor':
        courses = [course for course in courses if course.teacher.username == user_name]

    if user_role == 'estudiante':
        # courses = [course for course in courses if today < course.start_date]

        # if len(courses) == 0:
        #     courses = []

        try:
            student = get_object_or_404(Student, username=user_name) # Student.objects.get(username=user_name)
            print("Student : " + str(student))
        except Student.DoesNotExist:
            student = None
            registered_courses = []

        if student:
            # registered_courses = CourseStudent.objects.filter(student__username=user_name).values_list('course', flat=True)
            registered_courses = get_list_or_404(CourseStudent, student=student)
            registered_courses_filter = [course_student.course for course_student in registered_courses]

        # Filter the courses that have not started yet
        upcoming_courses = [course for course in courses if today < course.start_date]
    
        # Combine the registered courses with the upcoming courses
        # Use a set to avoid duplicates
        combined_courses = set(registered_courses_filter) | set(upcoming_courses)
    
        # Convert back to a list if needed
        courses = list(combined_courses)


    context = {
        'courses': courses,

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
