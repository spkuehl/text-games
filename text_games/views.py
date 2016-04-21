from django.shortcuts import render  # render a template to browser

def home(request):
    return render(request, "home.html")

def coming_soon(request):
    return render(request, "coming_soon.html")