from django.contrib import admin
from schema.models import Applicant, Course, Outline, Tutor

# Register your models here.
admin.site.register(Applicant)
admin.site.register(Course)
admin.site.register(Outline)
admin.site.register(Tutor)
