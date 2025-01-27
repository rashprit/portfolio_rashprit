from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    projects_show = [
        {
            'title': 'Multilingual Plagiarism Detection',
            'path': 'images/plagiarism_detection.PNG',
            'description': 'A project on detecting plagiarism across different languages using transformer-based models.'
        },
        {
            'title': 'Predictive Harvest Timing',
            'path': 'images/predictive_harvest.PNG',
            'description': 'AI-based model for predicting harvest timings, focusing on crop yield prediction.'
        },
    ]
    return render(request, "projects.html", {"projects_show": projects_show})

def research_work(request):
    return render(request, "research_work.html")

def certificate(request):
    return render(request, "certificate.html")

def contact(request):
    return render(request, "contact.html")

def resume(request):
    resume_path="myapp/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)

