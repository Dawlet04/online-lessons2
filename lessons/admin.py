from django.contrib import admin
from .models import Enrollment,Category, Course, Lesson, LessonProgress, Payment, Homework, HomeworkSubmission, Users, Teacher





admin.site.register(Teacher)
admin.site.register(Category)
admin.site.register(Enrollment)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(LessonProgress)
admin.site.register(Payment)
admin.site.register(Homework)
admin.site.register(HomeworkSubmission)
admin.site.register(Users)
# Register your models here.
