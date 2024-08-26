from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.contrib import messages
from ..models import Course, CourseStudent, Attendance
from django.urls import reverse
from datetime import datetime, timedelta

# Create your views here.
def index(request):
    courses = get_list_or_404(Course)

    context = {
        'courses': courses
    }

    return render(request, 'courses/index.html', context)

def course_detail(request, course_id):
    isOngoingCourse = True
    today = timezone.now().date() ## + timedelta(1)
    course = get_object_or_404(Course, pk=course_id)
    try:
        students = CourseStudent.objects.filter(course=course)       
    except:
        students = [] 

    try:
        attendance_records = Attendance.objects.filter(date=today, course_student__course=course)
        attendance_dict = {record.course_student_id: record for record in attendance_records}
    except Exception as e:
        attendance_dict = {}
        print(f"Error fetching attendance records: {e}")

    # Update students queryset with attendance status
    for student in students:
        student.attendance_today = attendance_dict.get(student.id, None)

    attendance_choices = Attendance.ATTENDANCE_CHOICES

    
    if today < course.start_date or today > course.end_date:
            isOngoingCourse = False
            messages.error(request, 'No se puede registrar la asistencia fuera de las fechas del curso.')     

    # Get the URL for adding a new student
    add_student_url = reverse('courses:add_course_student', args=[course.id])
    volverUrl = 'http://localhost:8000/courses/'

    context = {
        'course': course,
        'students': students,
        'add_student_url': add_student_url,
        'volverUrl': volverUrl,
        'isOngoingCourse':isOngoingCourse,
        'today':today,
        'attendance_choices': attendance_choices,
    }

    return render(request, 'courses/course_detail.html', context)    

def register_attendance(request, student_id):
    print("ingrsando ----->")
    if request.method == "POST":
        try:
            attendance_type = request.POST.get('attendance_type')
            student_course = get_object_or_404(CourseStudent, pk=student_id)
            print("ingrsando -----> 1111")
            # Verify if today's date is within the course's start and end dates
            today = timezone.now().date()
            course = student_course.course
            if today < course.start_date or today > course.end_date:
                messages.error(request, 'No se puede registrar la asistencia fuera de las fechas del curso.')
                return redirect('courses:course_detail', course_id=course.id)
            print("ingrsando -----> 22222")
            # Create a new attendance record
            Attendance.objects.create(
                course_student=student_course,
                date=today,
                type=attendance_type
            )
            print("ingrsando -----> 33333")
            messages.success(request, 'Asistencia registrada correctamente.')
        except Exception as e:
            print("ingrsando -----> 44444" + str(e))
            messages.error(request, f'Error al registrar la asistencia: {str(e)}')

        return redirect('courses:course_detail', course_id=course.id)
    