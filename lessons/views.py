from django.shortcuts import render
from .models import Course, Category, Teacher

def home(request):
    popular_courses = Course.objects.filter(is_published=True).order_by('-created_at')[:6]
    categories = Category.objects.all()
    teachers = Teacher.objects.all()[:4]
    context = {
        'popular_courses': popular_courses,
        'categories': categories,
        'top_teachers': teachers,
    }
    
    return render(request, 'base.html', context)

