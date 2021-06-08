from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from .models import Course, Teacher, Education


class AllCoursesView(View):
    courses = Course.objects.exclude(unlisted=True)

    def get(self, request):
        return render(request, "courses.html", context={
            "courses": self.courses
        })


class CourseView(DetailView):
    model = Course
    template_name = "course.html"
    def get_queryset(self):
        return Course.objects.all()


class TeacherView(DetailView):
    model = Teacher
    template_name = "teachers.html"
    def get_queryset(self):
        return Teacher.objects.all()


class EducationView(DetailView):
    model = Education
    template_name = "education.html"
    def get_queryset(self):
        return Education.objects.all()
