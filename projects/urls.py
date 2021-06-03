from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("projects", views.project_index, name="project_index"),
    path("project/<int:pk>/", views.project_detail, name="project_detail"),
    path("services", views.services_provided, name="services_provided"),
    path("about", views.about_me, name="about_me"),
    path("contact", views.contact, name="contact")
]