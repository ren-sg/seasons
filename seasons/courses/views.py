from django.views.generic import ListView
from .models import Course


class CoursesListView(ListView):
    model = Course
    template_name = "courses/courses_list.html"


courses_list_view = CoursesListView.as_view()
