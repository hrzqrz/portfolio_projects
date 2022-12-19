from django.shortcuts import render
from . models import Job
# Create your views here.

def jobs_home(request):
    jobs = Job.objects
    return render(request, 'jobs_home.html', {'jobs': jobs})
