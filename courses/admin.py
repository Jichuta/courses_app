from django.contrib import admin
from .models import Teacher, Student, Course, CourseStudent, Attendance

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'ci', 'age']

class CourseStudentAdmin(admin.ModelAdmin):
    list_display = ['course', 'student', 'grade', 'approved', 'isApproved']
    list_filter = ['course__name', 'approved']

# class AttendanceAdmin(admin.ModelAdmin):
#     list_display = ['course_student__student__name', 'course_student__course__name', 'date', 'type']
#     list_filter = ['course_student__course__name']

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['get_student_name', 'get_course_name', 'date', 'type']
    list_filter = ['course_student__course__name']

    def get_student_name(self, obj):
        return obj.course_student.student.name
    get_student_name.short_description = 'Student Name'

    def get_course_name(self, obj):
        return obj.course_student.course.name
    get_course_name.short_description = 'Course Name'

class CourseStudentInline(admin.TabularInline):
    model = CourseStudent
    extra = 3

# class CourseAdmin(admin.ModelAdmin):
#     list_display = ['name', 'teacher__name', 'start_date']
#     list_filter = ['name', 'teacher__name']

#     inlines = [CourseStudentInline]    
# 
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_teacher_name', 'start_date']
    list_filter = ['name', 'teacher__name']

    def get_teacher_name(self, obj):
        return obj.teacher.name
    get_teacher_name.short_description = 'Teacher Name'

    inlines = [CourseStudentInline]        

# Register your models here.
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(CourseStudent, CourseStudentAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register([Student,])
