from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from ..models import Course, Student, CourseStudent

def add_course_student(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        student_id = request.POST['student']
        grade = request.POST['grade']
        approved = grade and int(grade) > 50
        student = get_object_or_404(Student, pk=student_id)
        
        CourseStudent.objects.create(course=course, student=student, grade=grade, approved=approved)
        return redirect('courses:course_detail', course_id=course.id)

    students = Student.objects.exclude(coursestudent__course=course)
    return render(request, 'courses/add_course_student.html', {'course': course, 'students': students})
