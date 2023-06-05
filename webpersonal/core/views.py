from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request,"core/about.html")

def explorer(request):
    return render(request,"core/explorer.html")

def services(request):
    return render(request,"core/services.html")

