from django.urls import path, include
from .views      import StudentListView
from .views import ClassListView
from .views import CoursesListView
from .views import TeacherListView
urlpatterns = [
    path('student/', StudentListView.as_view(), name = 'student_list_view')
]
urlpatterns = [
    path('student/',ClassListView.as_view(), name = 'class_list_view')
]
urlpatterns = [
    path('student/',CoursesListView.as_view(), name = 'course_list_view')
]
urlpatterns = [
    path('student/',TeacherListView .as_view(), name = 'teacher_list_view')
]