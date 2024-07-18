from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import  StudentSerializer
from Classroom.models import classroom
from .serializers import  ClassesSerializer
from ClassPeriod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from course.models import course
from .serializers import CoursesSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
class StudentListView(APIView):
    def get(self,  request):
        Students = Student.objects.all()
        serializer = StudentSerializer(Students, many=True)
        return Response(serializer.data)
class ClassListView(APIView):
    def get(self,  request):
        Classes = Classes.objects.all()
        serializer = ClassesSerializer(Students, many=True)
        return Response(serializer.data)
class ClassPeriodListView(APIView):
    def get(self, request):
        ClassPeriod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(ClassPeriod, many = True)
        return Response(serializer.data)
class CoursesListView(APIView):
    def get(self, request):
        Courses = Courses.objects.all()
        serializer = CoursesSerializer(Courses, many = True)
        return Response(serializer.data)
class TeacherListView(APIView):
    def get(self, request):
        Teacher = Teacher.objects.all()
        serializer = TeacherSerializer(Teacher, many = True)
        return Response(serializer.data)
























