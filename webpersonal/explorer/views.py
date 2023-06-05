from django.shortcuts import render
from .models import Explorer

# Create your views here.
def explorer(request):
    explorer= Explorer.objects.all()
    return render(request,"explorer/explorer.html",{'lugares':explorer})