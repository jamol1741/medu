from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView

from .views import CourseView, AllCoursesView, TeacherView, EducationView, AllEducationsView, AllTeachersView

urlpatterns = [
    # path('__admin/', admin.site.urls),

    # static
    path('', AllCoursesView.as_view(), name="courses"),
    path('educations/', AllEducationsView.as_view(), name="educations"),
    path('teachers/', AllTeachersView.as_view(), name="teachers"),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('<slug:slug>/', CourseView.as_view(), name="course"),
    path('educations/<int:pk>', EducationView.as_view(), name="education"),
    path('teachers/<int:pk>', TeacherView.as_view(), name="teacher"),
]

