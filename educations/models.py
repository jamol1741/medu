from datetime import datetime

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class CertificateName(models.Model):
    SCORE = 'score'
    LEVEL = 'level'
    DEGREE = 'degree'
    FIELDS = (
        (SCORE, 'Score'),
        (LEVEL, 'Level'),
        (DEGREE, 'Degree')
    )
    title = models.CharField(max_length=128)
    field_name = models.CharField(max_length=32, choices=FIELDS)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    name = models.ForeignKey(CertificateName, on_delete=models.CASCADE)
    score = models.DecimalField(decimal_places=1, null=True, blank=True, max_digits=5)
    level = models.CharField(max_length=16, null=True, blank=True)
    degree = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name.title


class Teacher(models.Model):
    MALE = 'male'
    FEMALE = 'female'

    GENDERS = (
        (MALE, "Male"),
        (FEMALE, "Female")
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=16, choices=GENDERS)
    date_of_birth = models.DateField(null=True, blank=True)
    certificates = models.ManyToManyField(Certificate, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name


class Location(models.Model):
    lat = models.CharField(max_length=128)
    lng = models.CharField(max_length=128)
    accuracy = models.IntegerField()

    def __str__(self):
        return self.lat + ' ' + self.lng


class Education(models.Model):
    title = models.CharField(max_length=512)
    description = models.CharField(max_length=2048)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,
                                 null=True, blank=True)
    teachers = models.ManyToManyField(Teacher, blank=True)

    def __str__(self):
        return self.title


class CourseType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class CourseLength(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class CourseTag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class RatePlan(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class TimeTable(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    @property
    def duration(self):
        total_seconds = int(self.end_time.second - self.start_time.second)
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60

        return '{} hours {} min'.format(hours, minutes)

    def __str__(self):
        return self.start_time.__str__() + ' - ' + self.end_time.__str__()


class Weekday(models.Model):
    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'

    WEEKDAYS = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday')
    )
    day = models.CharField(max_length=32, choices=WEEKDAYS)
    time_tables = models.ManyToManyField(TimeTable)


class WeeklySchedule(models.Model):
    days = models.ManyToManyField(Weekday)


class TypeOfEducation(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(null=False, unique=True)
    description = models.CharField(max_length=1024)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)

    unlisted = models.BooleanField(default=False, blank=True)

    course_type = models.ManyToManyField(CourseType)
    start_date = models.DateField(null=True, blank=True)
    course_length = models.ForeignKey(CourseLength, on_delete=models.CASCADE)
    tags = models.ManyToManyField(CourseTag, blank=True)
    price = models.CharField(max_length=128)
    rate_plan = models.ForeignKey(RatePlan, on_delete=models.CASCADE)
    type_of_education = models.ManyToManyField(TypeOfEducation)

    published_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    @property
    def get_type_of_education(self):
        course = Course.objects.filter(id=self.id)[0]

        return ', '.join([type_edu.title for type_edu in Course.objects.get(id=course.id).type_of_education.all()])

    @property
    def url(self):
        return reverse('course', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    @property
    def prev(self):
        return Course.objects.filter(id__lt=self.id)

    @property
    def prev(self):
        return Course.objects.filter(id__gt=self.id)


