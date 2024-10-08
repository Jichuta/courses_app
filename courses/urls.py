from django.urls import path, re_path
from django.shortcuts import redirect
from . import view
from .views.views_students import save_student
from .views.views_teacher import save_teacher, delete_teacher
from .views.view_course import add_course, delete_course
from .views.views_courses import course_detail, register_attendance
from .views.views_coursestudent import add_course_student
from .views.views_user import login_page, user_login, user_logout

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
    path('login/',login_page, name='login_page'),
    path('user_login', user_login, name='user_login'),
    path('logout', user_logout, name='user_logout'),
    path('course/<int:course_id>/delete/', delete_course, name="delete_course"),
    path('<int:teacher_id>/delete/', delete_teacher, name="delete_teacher"),
    path('register-attendance/<int:student_id>/', register_attendance, name='register_attendance'),

    # Catch-all pattern to redirect to login_page
    re_path(r'^.*$', lambda request: redirect('courses:login_page'), name='catch_all'),
]