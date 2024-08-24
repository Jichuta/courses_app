from django.urls import path
from . import view
from .views.views_students import save_student
from .views.views_teacher import save_teacher
from .views.view_course import add_course
from .views.views_courses import course_detail
from .views.views_coursestudent import add_course_student

app_name = 'courses'
urlpatterns = [
    path('', view.index, name='index'),
    # path('<int:course_id>', view.course_detail, name='course_detail'),
    path('<int:course_id>', course_detail, name='course_detail'),
    path('student/', view.students, name='students'),
    path('save_student/', save_student, name='save_student'),
    path('teacher/', view.teachers, name='teacher'),
    path('save_teacher/', save_teacher, name='save_teacher'),
    path('add_course/', add_course, name='save_course'),
    # path('course/<int:course_id>/', course_detail, name='course_detail'),
    path('<int:course_id>/add_student/', add_course_student, name='add_course_student'),
]