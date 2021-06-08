from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path('__admin/', admin.site.urls),

    path('', include('educations.urls')),
]