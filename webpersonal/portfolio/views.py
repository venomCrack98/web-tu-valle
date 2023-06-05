from django.shortcuts import render
from .models import Project

# Create your views here.
def contact(request):
    projects= Project.objects.all()
    return render(request,"portfolio/contact.html",{'projects':projects})