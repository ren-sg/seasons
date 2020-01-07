from django.urls import path

from seasons.courses.views import courses_list_view

app_name = "courses"
urlpatterns = [path("", view=courses_list_view, name="list")]
