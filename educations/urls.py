from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required

from .views import CourseView, AllCoursesView, TeacherView, EducationView

urlpatterns = [
    # path('__admin/', admin.site.urls),

    # static
    path('', AllCoursesView.as_view(), name="courses"),
    path('<slug:slug>/', CourseView.as_view(), name="course"),
    path('educations/<int:pk>', EducationView.as_view(), name="education"),
]

