from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("projects/", views.projects, name="projects"),
    path("research_work/", views.research_work, name="research_work"),
    path("certificate/", views.certificate, name="certificate"),
    path("contact/", views.contact, name="contact"),
    path("resume/", views.resume, name="resume"),
]
