from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=200)
    ci = models.IntegerField(default=0)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    ci = models.IntegerField()

    def __str__(self):
        return '{} (CI: {})'.format(self.name, self.ci)

class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    start_date = models.DateField()

    def __str__(self):
        return self.name

class CourseStudent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.IntegerField(default=0)
    approved = models.BooleanField()

    @property
    def isApproved(self):
        return self.grade > 50

    def __str__(self):
        return '{} ({})'.format(self.student, self.course)

class Attendance(models.Model):
    PRESENT = "P"
    LATE = "L"
    EXCUSED = "E"
    ABSENT = "A"
    ATTENDANCE_CHOICES = [
        (PRESENT, "Present"),
        (LATE, "Late"),
        (EXCUSED, "Excused"),
        (ABSENT, "Absent"),
    ]      
    course_student = models.ForeignKey(CourseStudent, on_delete=models.CASCADE)
    date = models.DateField()
    type = models.CharField(
        max_length = 2,
        choices=ATTENDANCE_CHOICES,
        default = ABSENT
    )

    def __str__(self):
        return '{} - {} ({})'.format(
            self.course_student.student.name,
            self.date,
            self.type
        )
