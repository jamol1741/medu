from django.contrib import admin
from .models import (Course, CourseType, TypeOfEducation,
                     CourseTag, CourseLength, TimeTable,
                     Weekday, Education, RatePlan, Teacher,
                     Certificate, CertificateName, Location,
                     WeeklySchedule)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseType)
admin.site.register(TypeOfEducation)
admin.site.register(CourseTag)
admin.site.register(CourseLength)
admin.site.register(TimeTable)
admin.site.register(Weekday)
admin.site.register(Education)
admin.site.register(RatePlan)
admin.site.register(Teacher)
admin.site.register(Certificate)
admin.site.register(CertificateName)
admin.site.register(Location)
admin.site.register(WeeklySchedule)